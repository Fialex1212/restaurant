from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django import forms
from .models import BookTabel


class CallbackForm(forms.Form):
    name = forms.CharField(
        label="Full Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your name",
                "class": "form__input form__full-name",
            }
        ),
    )
    phone = forms.CharField(
        label="Phone number",
        max_length=15,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your phone number",
                "class": "form__input form__phone-number",
            }
        ),
    )
    message = forms.CharField(
        label="Message",
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Max 120 symbols",
                "class": "form__input form__message",
            }
        ),
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
