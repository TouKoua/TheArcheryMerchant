from django.shortcuts import render
from django.views import View

Bow = None
Arrow = None

class Home(View):
    def get(self,request):
        return render(request, "home.html", {})
    
    def post(self, request):
        global Bow
        global Arrow
        if not request.POST["bow"]:
            arrow = request.POST["arrow"]
            Arrow = request.POST["arrow"]
            if not Bow:
                bow = None
            else:
                bow = Bow
        else:
            bow = request.POST["bow"]
            Bow = request.POST["bow"]
            if not Arrow:
                arrow = None
            else:
                arrow = Arrow
        return render(request, "home.html", {"bow": bow, "arrow": arrow})