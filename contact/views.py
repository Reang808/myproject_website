from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # データベースに保存
            Contact.objects.create(
                company=form.cleaned_data['company'],
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                contact_method=form.cleaned_data['contact_method'],
                contact_date=form.cleaned_data['contact_date'],
                message=form.cleaned_data['message'],
            )
            user_email = form.cleaned_data['email']
            user_name = form.cleaned_data['name']

            # ユーザーへの自動返信
            subject = '【Reang】お問い合わせありがとうございます'
            message = (
                f"{user_name} 様\n\n"
                "この度はお問い合わせいただきありがとうございます。\n"
                "内容を確認のうえ、1営業日以内にご返信いたします。\n\n"
                "※このメールは自動送信です。\n"
                "----------------------------------\n"
                "Reang サポート"
            )
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
                fail_silently=False,
            )

            # 管理者への通知メール
            admin_subject = '【Reang】新しいお問い合わせがありました'
            admin_message = (
                f"会社名・サロン名: {form.cleaned_data['company']}\n"
                f"お名前: {user_name}\n"
                f"メールアドレス: {user_email}\n"
                f"電話番号: {form.cleaned_data['phone']}\n"
                f"希望連絡方法: {form.cleaned_data['contact_method']}\n"
                f"希望連絡日時: {form.cleaned_data['contact_date']}\n"
                f"お問い合わせ内容:\n{form.cleaned_data['message']}\n"
            )
            send_mail(
                admin_subject,
                admin_message,
                settings.DEFAULT_FROM_EMAIL,
                ['info@reang.jp'],  # ←ここをあなたの管理用メールアドレスに
                fail_silently=False,
            )

            return render(request, 'contact/contact_index.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact/contact_index.html', {'form': form})