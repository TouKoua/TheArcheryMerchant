from django.shortcuts import render
from django.views import View
from django import forms
from django import forms
from TheArcheryMerchant.models import Bow, Arrows

class BowForm(forms.ModelForm):
    drawlength = forms.IntegerField(required=False)
    drawstrength = forms.IntegerField(required=False)
    
    class Meta:
        model = Bow
        fields = {"bowtype", "drawlength", "drawstrength"}

class ArrowForm(forms.ModelForm):
    arrowLength = forms.CharField(required=False)
    spinage = forms.CharField(required=False)
    
    class Meta:
        model = Arrows
        fields={"arrowLength", "spinage"}

class selectionPage(View):
    def get(self, request, itemname):
        if(itemname == "Bow"):
            form = BowForm
        else:
            form = ArrowForm
        return render(request, "selectionPage.html", {"form": form})