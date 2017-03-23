from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext
from app01.forms.accountform import LoginForm
import json


# Create your views here.
def Index(request):
    return HttpResponse('<h1>hello world!</h1>')


def Auth(request):
    print request.GET
    user, passwd = request.GET['username'], request.GET['passwd']
    if user == "djj" and passwd == "123456":
        return HttpResponse('welcome user %s login in' % user)
    else:
        return HttpResponse('your account or password is worry')


def Login(request):
    if request.method == 'POST':
        data = request.POST
        logindata = LoginForm(data)
        if logindata.is_valid():
            return HttpResponse('ok')
        else:
            return render(request, 'index.html', {'model': logindata})
    logindata = LoginForm()
    return render(request, 'index.html', {'model': logindata})


def Menu(request):
    region_dict = {
            'shandong': {
                'JiNan': ['JiNing', 'YunCheng'],
                'DeZhou': ['LeLing', 'NiJing']
                },
            'HeNan': {
                'XinYang': ['djj', 'ddsa'],
                }
            }
    return HttpResponse(json.dumps(region_dict))
