from django.shortcuts import render



def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")

def contacts(request):
    data = {"values": ["OPENING TIMES", "MON - SUN 10:00 - 18:00", "LOCATION", "Opp. Burj Al Arab, Jumeirah St, Umm Suqeim 3, Dubai", "CONTACT", "+971 4 348 4444", "wwguestrelations@wildwadi.com"]}
    return render(request, "main/contacts.html", data)

