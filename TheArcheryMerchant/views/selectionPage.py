from django.shortcuts import render
from django.views import View
from django import forms
from TheArcheryMerchant.models import Bow, Arrows

class BowForm(forms.ModelForm):
    drawlength = forms.IntegerField(required=False)
    drawstrength = forms.IntegerField(required=False)
    price = forms.IntegerField(required=False)
    
    class Meta:
        model = Bow
        fields = {"bowtype", "drawlength", "drawstrength", "price", "sellers"}
    
    field_order = ["bowtype", "drawlength", "drawstrength", "price", "sellers"]

class ArrowForm(forms.ModelForm):
    arrowLength = forms.CharField(required=False)
    spinage = forms.CharField(required=False)
    price = forms.IntegerField(required=False)
    
    class Meta:
        model = Arrows
        fields={"arrowLength", "spinage", "price", "sellers"}
    
    field_order = ["arrowLength", "spinage", "price", "sellers"]
    
class bowSelection(View):
    def get(self, request):
        form = BowForm
        bowlist = Bow.objects.all()
        return render(request, "bowSelection.html", {"form": form, "bowlist": bowlist})
    
    def post(self, request):
        form = BowForm
        bowlist = Bow.objects.all()
        return render(request, "bowSelection.html", {"form": form, "bowlist": bowlist})
    
class arrowSelection(View):
    def get(self, request):
        form = ArrowForm
        arrowlist = Arrows.objects.all()
        return render(request, "arrowSelection.html", {"form": form, "arrowlist": arrowlist })
    
    def post(self, request):
        form = ArrowForm
        arrowlist = Arrows.objects.all()
        return render(request, "arrowSelection.html", {"form": form, "arrowlist": arrowlist })