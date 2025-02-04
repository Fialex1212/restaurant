from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django import forms
from .models import BookTabel


class CallbackForm(forms.Form):
    name = forms.CharField(
        label="Имя",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Введите ваше имя"}),
    )
    phone = forms.CharField(
        label="Телефон",
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Введите ваш телефон"}),
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookTabel
        fields = ["name", "phone", "date", "time", "guests", "comment"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "phone": forms.TextInput(attrs={"placeholder": "+380 XX XXX XXXX"}),
        }
