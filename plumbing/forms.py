from django import forms
from captcha.fields import ReCaptchaField
from .models import Contact


class ContactModelForm(forms.ModelForm):
    def __init__(self):
        super(ContactModelForm, self).__init__()
        self.fields['captcha'] = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

