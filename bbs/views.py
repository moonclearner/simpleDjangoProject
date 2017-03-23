from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse


def Bbs(request):
    return render_to_response("bbs.html")
