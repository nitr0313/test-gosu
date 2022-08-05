from pyexpat import model
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'bday', 'passport_num', 'oms', 'snils']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['passport_num'].widget = forms.TextInput(attrs={
            "pattern": r"\d{4}\s{1}\d{6}",
            "class": "form-control"
        })
        self.fields['passport_num'].widget = forms.TextInput(attrs={
            "pattern": r"\d{3}\-\d{3}\-\d{3}\s{1}\d{2}",
            "class": "form-control"
        })