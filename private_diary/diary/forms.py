from django import forms

# Djangoで用意されているメールを送信する機能
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル',max_length=30)
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)
    
    def __init__ (self,*args,**kwargs):

        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'forms-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください'

        self.fields['email'].widget.attrs['class'] = 'forms-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください'

        self.fields['title'].widget.attrs['class'] = 'forms-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください'

        self.fields['message'].widget.attrs['class'] = 'forms-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください'

    # メール送信メソッドを追加する
    def send_mail(self):
