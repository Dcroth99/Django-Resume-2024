from django import forms
from .models import InputForm

class LoginForm(forms.ModelForm):
    class Meta:
        model = InputForm
        fields = '__all__'