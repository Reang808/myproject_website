from django import forms

class ContactForm(forms.Form):
    company = forms.CharField(label='会社名・サロン名', max_length=100, required=False)
    name = forms.CharField(label='お名前', max_length=50)
    email = forms.EmailField(label='メールアドレス')
    phone = forms.CharField(label='電話番号', max_length=20, required=False)
    contact_method = forms.ChoiceField(
        label='希望連絡方法',
        choices=[('email', 'メール'), ('phone', '電話')],
        widget=forms.Select   # ← ここを変更
    )
    contact_date = forms.DateField(label='希望連絡日時', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)