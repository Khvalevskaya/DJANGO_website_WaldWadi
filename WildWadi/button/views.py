from django.shortcuts import render
from .models import Articles


def button_home(request):
    button = Articles.objects.all()
    return render(request, "button/button_home.html", {"button": button})


def total_price(request):
    adult_num = request.GET["adult"]
    child_num = request.GET["child"]
    date = request.GET["day"]
    month = request.GET["month"]
    year = request.GET["year"]
    total = request.GET["totalPrice"]
    print(total)

    return render(request, "button/total_price.html", {"adult": adult_num, "child": child_num, "day": date, "month": month, "year": year, "totalPrice": total})
