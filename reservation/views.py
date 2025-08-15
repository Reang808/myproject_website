from django.shortcuts import render
from .forms import ReservationForm
from django.core.mail import send_mail
from django.conf import settings

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            # 自動返信メール
            subject = '【Reang】ご予約ありがとうございます'
            message = (
                f"{reservation.name} 様\n\n"
                f"ご予約を受け付けました。\n"
                f"予約日時: {reservation.date} {reservation.time}\n"
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
                f"予約日時: {reservation.date} {reservation.time}\n"
                f"その他: {reservation.other_field if hasattr(reservation, 'other_field') else 'なし'}\n\n"
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