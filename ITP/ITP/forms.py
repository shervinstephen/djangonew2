from django import forms
from .models import ChargeInsert


class chargeform(forms.ModelForm):
    class Meta:
        model=ChargeInsert
        fields="__all__"