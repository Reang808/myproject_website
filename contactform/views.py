from django.shortcuts import render

def reservation(request):
    from django.core.mail import send_mail
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        message = request.POST.get('message')
        subject = f"お問い合わせ: {name}様"
        body = f"お名前: {name}\nメール: {email}\n電話番号: {phone}\n会社名: {company}\n\n内容:\n{message}"
        try:
            send_mail(
                subject,
                body,
                email,  # 送信者
                ['info@reang.jp'],
                fail_silently=False,
            )
            context['success'] = True
        except Exception as e:
            context['error'] = str(e)
    return render(request, 'contactform/reservation.html', context)
