from django.shortcuts import render

def button_home(request):
    return render(request, "button/button_home.html")
