from django.shortcuts import render
from heart.models import Htem
from django.http import HttpResponse
import json

# Create your views here.


def Heart(request):
    valid = False
    Account = ''
    if request.method == "POST":
        if 'out' in request.POST:
            valid = False
        else:
            Account = request.POST.get('account')
            Password = request.POST.get('password')
            print Account, Password
            valid = True
    #  TEM = Htem.objects.order_by('id')[:3]
    TEM = Htem.objects.order_by("-id").values_list('id', 'values')[:2]
    return render(request, "human.html", {'valid': valid, 'account': Account, 'temp': TEM})


def htem(request):
    #  TEM = Htem.objects.order_by("-id").values_list('id', 'values')[:5]
    #  htemdict = {}
    #  for i in TEM:
    #      htemdict[int(i[0])] = float(i[1])
    #  temp_json = json.dumps(htemdict)
    #  if request.is_ajax() and request.method == 'GET':
    #      return HttpResponse(temp_json, content_type="application/json")
    #  else:
    #      return HttpResponse("ok")
    path = 'D:\\python-project\\wed_dev\\django\\simpleDjangoProject\\heart\\tem_normal.txt'
    f = open(path)
    data = f.read()
    data = data.split(",")
    length = len(data)
    tem_dict = dict(zip(range(length), data))
    temp_json = json.dumps(tem_dict)
    if request.is_ajax() and request.method == 'GET':
        return HttpResponse(temp_json, content_type="application/json")
    else:
        return HttpResponse("ok")
