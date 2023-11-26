from django.shortcuts import render
from django.views import View
from django import forms
from TheArcheryMerchant.models import Bow, Arrows

class BowForm(forms.Form):
    author = forms.CharField(initial="", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    publisher = forms.CharField(initial="", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    available = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)

class Home(View):
    def get(self,request):
        return render(request, "home.html", {})