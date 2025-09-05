from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label='名前', max_length=100, required=True)
	email = forms.EmailField(label='メールアドレス', required=True)
	phone = forms.CharField(label='電話番号', max_length=20, required=False)
	inquiry_type = forms.ChoiceField(
		label='問い合わせ項目',
		choices=[
			('general', 'システム導入'),
			('support', 'ご相談'),
			('feedback', 'その他'),
		],
		required=True
	)
	plan = forms.ChoiceField(
		label='プラン選択',
		choices=[
			('', '選択してください'),
			('basic', '未定'),
			('standard', 'LINE連携'),
			('premium', 'LINE連携＋システム'),
			('enterprise', 'Webサイト制作＋システム'),
			('custom', 'Webサイト制作＋予約システム＋システム'),

		],
		required=False
	)
	message = forms.CharField(label='問い合わせ内容', widget=forms.Textarea, required=True)
