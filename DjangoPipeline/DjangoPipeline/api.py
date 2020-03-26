from __future__ import unicode_literals
from django.http import JsonResponse
import json

def jsonres(data=None, result=True, reason=None):
    res = dict()
    if result:
        if data:
            res['data'] = data
            res['code'] = 0
            res['msg'] = 'ok'
            return JsonResponse(res)
        else:
            res['code'] = -1
            res['msg'] = 'no data'
            return JsonResponse(res)
    else:
        res['code'] = 1
        res['msg'] = reason or 'error'
    return JsonResponse(res)

def test(request):
    if request.method == 'POST':  # request type
        req = json.loads(request.body)
        # def deal function return xxx
        return jsonres(req)
    else:
        return jsonres(result=False)