
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            inquiry_type = form.cleaned_data['inquiry_type']
            plan = form.cleaned_data['plan']
            message = form.cleaned_data['message']

            subject = f'お問い合わせ: {inquiry_type} ({plan})'
            body = f'名前: {name}\nメール: {email}\n電話番号: {phone}\n問い合わせ項目: {inquiry_type}\nプラン: {plan}\n内容:\n{message}'
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return render(request, 'contact/contact.html', {'form': ContactForm(), 'success': True})
        else:
            return render(request, 'contact/contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})