from django.db import models

# Create your models here.

class Contact(models.Model):
    company = models.CharField('会社名・サロン名', max_length=100, blank=True)
    name = models.CharField('お名前', max_length=50)
    email = models.EmailField('メールアドレス')
    phone = models.CharField('電話番号', max_length=20, blank=True)
    contact_method = models.CharField('希望連絡方法', max_length=10, choices=[('email', 'メール'), ('phone', '電話')])
    contact_date = models.DateField('希望連絡日時', blank=True, null=True)
    message = models.TextField('お問い合わせ内容')
    created_at = models.DateTimeField('送信日時', auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
