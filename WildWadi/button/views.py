from django.shortcuts import render
from .models import Articles


def button_home(request):
    button = Articles.objects.all()

    # tickets = {"standart_adult": [249, 100],
    #            "standart_child": [219, 100],
    #            "combo_adult": [275, 100]}

    return render(request, "button/button_home.html", {"button": button})
