from django.shortcuts import render
from django.views import View
from TheArcheryMerchant.models import Bow, Arrows

selectedBow = None
selectedArrow = None

class Home(View):
    def get(self,request):
        total = 0
        return render(request, "home.html", {"total": total})
    
    def post(self, request):
        global selectedBow
        global selectedArrow
        issues = []
        total = 0
        if not request.POST.get("bow"):
            arrow = Arrows.objects.get(name=request.POST["arrow"])
            selectedArrow = arrow
            if not selectedBow:
                bow = None
            else:
                bow = selectedBow
        else:
            bow = Bow.objects.get(name=request.POST["bow"])
            selectedBow = bow
            if not selectedArrow:
                arrow = None
            else:
                arrow = selectedArrow
        if selectedBow:
            total += selectedBow.price
        if selectedArrow:
            total += selectedArrow.price
            
        if selectedArrow and selectedBow:
            if selectedArrow.arrowLength < selectedBow.drawLength:
                issues.append("Arrow length smaller than bow max draw length!")
            if selectedArrow.arrowLength > selectedBow.drawLength + 4:
                issues.append("Arrow length greater than bow max draw length by 5 inches!")
                # Need to add conditiona for arrow spine and bow draw strength
        return render(request, "home.html", {"bow": bow, "arrow": arrow, "total": total, "errors": issues})