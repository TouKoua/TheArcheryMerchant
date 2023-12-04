from django.shortcuts import render
from django.views import View
from django import forms
from django import forms
from TheArcheryMerchant.models import Bow, Arrows

class BowForm(forms.ModelForm):
    drawlength = forms.IntegerField(required=False)
    drawstrength = forms.IntegerField(required=False)
    price = forms.IntegerField(required=False)
    
    class Meta:
        model = Bow
        fields = {"bowtype", "drawlength", "drawstrength", "price", "sellers"}

class ArrowForm(forms.ModelForm):
    arrowLength = forms.CharField(required=False)
    spinage = forms.CharField(required=False)
    price = forms.IntegerField(required=False)
    
    class Meta:
        model = Arrows
        fields={"arrowLength", "spinage", "price", "sellers"}

class selectionPage(View):
    def get(self, request, itemname):
        print(itemname)
        if(itemname == "Bow"):
            form = BowForm
            bowlist = Bow.objects.all()
            arrowlist = []
        else:
            form = ArrowForm
            arrowlist = Arrows.objects.all()
            bowlist = []
        return render(request, "selectionPage.html", {"form": form, "bowlist": bowlist, "arrowlist": arrowlist})