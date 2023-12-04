from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self,request):
        return render(request, "home.html", {})
    
    def post(self, request):
        if not request.POST["bow"]:
            arrow = request.POST["arrow"]
        else:
            bow = request.POST["bow"]
        return render(request, "home.html", {"bow": bow, "arrow": arrow})