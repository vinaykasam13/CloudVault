from django.shortcuts import render

from pyexpat.errors import messages


def index(request):
    return render(request,"index.html")


