from django.shortcuts import render
from .models import Articles


def button_home(request):
    button = Articles.objects.all()
    return render(request, "button/button_home.html", {"button": button})


# def total_price(request):
#     adult_num = request.GET["adult"]
#     child_num = request.GET["child"]
#     type = request.GET
#     tickets = {"standart_adult": [249, 100],
#                "standart_child": [219, 100],
#                "combo_adult": [275, 100],
#                "combo_child": [255, 100]}
#
#     return render(request, "button/total_price.html", {"adult": adult_num, "child": child_num})
