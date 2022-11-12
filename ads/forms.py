from django import forms

from ads.models import Ads


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = '__all__'
