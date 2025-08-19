from django.http import JsonResponse
from .models import TimeSlot
# 日付ごとの空きタイムスロットを返すAPI
from django.views.decorators.http import require_GET
@require_GET
def available_timeslots(request):
    from datetime import datetime, timedelta, time as dtime
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({'error': 'date parameter required'}, status=400)
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return JsonResponse({'error': 'invalid date format'}, status=400)
    today = datetime.today().date()
    one_month_later = today + timedelta(days=31)
    if not (today <= date_obj <= one_month_later):
        return JsonResponse({'times': []})
    # TimeSlotが1つもなければ自動生成
    slots = TimeSlot.objects.filter(date=date_obj)
    if not slots.exists():
        for h in range(10, 23):
            TimeSlot.objects.create(date=date_obj, time=dtime(hour=h, minute=0))
        slots = TimeSlot.objects.filter(date=date_obj)
    all_times = [f"{h:02d}:00" for h in range(10, 23)]
    available_hours = set(slot.time.hour for slot in slots if not slot.is_booked)
    available_times = [f"{h:02d}:00" for h in range(10, 23) if h in available_hours]
    return JsonResponse({'times': available_times})
from django.shortcuts import render
from .forms import ReservationForm
from django.core.mail import send_mail
from django.conf import settings
# views.py
from django.http import JsonResponse
from .models import Reservation
from .models import TimeSlot

def timeslot_events(request):
    events = []
    for slot in TimeSlot.objects.all():
        if slot.is_booked:
            events.append({
                "title": "予約済み",
                "start": f"{slot.date}T{slot.time}",
                "color": "red"
            })
    return JsonResponse(events, safe=False)

def reservation_events(request):
    events = []
    for r in Reservation.objects.all():
        events.append({
            "title": "予約済み",
            "start": f"{r.date}T{r.time}",  # ISO形式
            "color": "red"
        })
    return JsonResponse(events, safe=False)
def reservation(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        selected_time = post_data.get('time')
        form = ReservationForm(post_data)
        if form.is_valid() and selected_time:
            reservation = form.save(commit=False)
            reservation.time = selected_time
            reservation.save()
            # 自動返信メール
            subject = '【Reang】ご予約ありがとうございます'
            message = (
                f"{reservation.name} 様\n\n"
                f"ご予約を受け付けました。\n"
                f"予約日時: {reservation.date} {selected_time}\n"
                "内容を確認のうえ、1営業日以内にご連絡いたします。\n\n"
                "※このメールは自動送信です。\n"
                "----------------------------------\n"
                "Reang サポート"
            )
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [reservation.email],
                fail_silently=False,
            )
            admin_subject = '【Reang】新しい予約が入りました'
            admin_message = (
                f"新しい予約がありました。\n\n"
                f"お名前: {reservation.name}\n"
                f"メール: {reservation.email}\n"
                f"予約日時: {reservation.date} {selected_time}\n"
                f"その他: {reservation.message}\n\n"
                "管理画面から詳細を確認してください。"
            )
            send_mail(
                admin_subject,
                admin_message,
                settings.DEFAULT_FROM_EMAIL,
                ['praxisweb365@gmail.com'],  # 例: ['info@yourdomain.com']
                fail_silently=False,
            )
            return render(request, 'reservation/reservation_done.html')
    else:
        form = ReservationForm()
    return render(request, 'reservation/reservation_form.html', {'form': form})