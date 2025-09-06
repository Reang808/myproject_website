
from django.db import models

class Contact(models.Model):
	name = models.CharField('名前', max_length=100)
	email = models.EmailField('メールアドレス')
	phone = models.CharField('電話番号', max_length=20, blank=True)
	inquiry_type = models.CharField(
		'問い合わせ項目',
		max_length=20,
		choices=[
			('service', '申し込み'),
			('general', '料金について'),
			('support', 'ご相談'),
			('feedback', 'その他'),
		]
	)
	plan = models.CharField(
		'プラン選択',
		max_length=20,
		choices=[
			('basic', '未定'),
			('standard', 'LINE連携'),
			('premium', 'LINE連携＋システム'),
			('enterprise', 'Webサイト制作＋システム'),
			('custom', 'Webサイト制作＋予約システム＋システム'),
		],
		blank=True
	)
	message = models.TextField('問い合わせ内容')
	created_at = models.DateTimeField('送信日時', auto_now_add=True)

	def __str__(self):
		return f"{self.name} ({self.email})"

# Create your models here.
