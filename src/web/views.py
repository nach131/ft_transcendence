from django.shortcuts import render


def home(req):
    return render(req, "home.html")


def botones(req):
    # data = {"nombre": "Pedro", "apellido": "Papiedrra", "edad": 42}
    # return render(req, "toma.html", {"data": data})
    return render(req, "botones/index.html")


def about_us(req):
    # daabout_usta = {"nombre": "Pedro", "apellido": "Papiedrra", "edad": 42}
    # return render(req, "toma.html", {"data": data})
    return render(req, "about_us/index.html")
