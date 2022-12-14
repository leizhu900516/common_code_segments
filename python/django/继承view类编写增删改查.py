# -*- coding: utf-8 -*-
# @author: chenhuachao
# @Time: 2022/12/14 -14:46
# Filename: 继承view类编写增删改查.py
# Desc:
from django.views.generic import View
class SignLogManage(View):
    def get(self, request):
        data= {}
        return JsonResponse(data)

    def delete(self, request):
        data= {}
        return JsonResponse(data)
    def put(self,request):
        pass
    def post(self,request):
        pass
