# coding:utf-8
import json


f = open(u"心电正常（65）.txt")
data = f.read()
if data:
    jsonInt = []
    datajson = []
    jsontxt = data.split(",")
    #  print jsontxt, len(jsontxt)
    for i in jsontxt:
        jsonInt.append(float(i))
    length = len(jsonInt)
    lenlist = range(length)
    celllist = []
    for i in range(length):
        celllist = [str(lenlist[i]), jsonInt[i]]
        datajson.append(celllist)
    print datajson
    json.dump(datajson, open("data65.json", "w"))
f.close()
