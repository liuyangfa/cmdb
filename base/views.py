# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from base.models import System


# Create your views here.

def redirect(request):
    return render(request, "login.html")


@csrf_exempt
def login(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session["user"] = username
            # response = HttpResponseRedirect('/index/')
            return HttpResponse("OK")
        else:
            return render(request, "login.html", {"error": "用户名或密码错误"})
    if request.method == 'GET':
        return render(request, "login.html")


@login_required
def index(request):
    username = request.session.get("user", "")
    return render(request, "index.html", {"user": username})


def member_list(request):
    all_list = System.objects.filter().all()
    return render(request, "member-list.html", {'list': all_list})


@csrf_exempt
def member_add(request):
    result = request.body

    if result == "":
        return render(request, "member-add.html")
    else:
        print(request.POST)
        if request.method == 'POST':
            sql_id = request.POST.get("sql_id", 1001)
            enname = request.POST.get("enname", 1002)
            cnname = request.POST.get("cnname", 1003)
            System(sql_id=sql_id, enname=enname, cnname=cnname).save()
        return render(request, "member-list.html")


@csrf_exempt
def member_del(request):
    result = request.body

    if result == "":
        return render(request, "member-del.html")
    else:
        print(request.POST)
        if request.method == 'POST':
            id = request.POST.get("id", None)
            if id != None:
                System.objects.filter(id=id).delete()
                print(System.objects.filter(id=id))
        return render(request, "member-list.html")


@csrf_exempt
def member_edit(request, id):
    if request.body == "" and id != "":
        obj = System.objects.filter(id=id)
        return render(request, "member-edit.html", {"obj": obj})
    elif request.body != "" and id != "":
        if request.method == 'POST':
            sql_id = request.POST.get("sql_id", 1001)
            enname = request.POST.get("enname", 1002)
            cnname = request.POST.get("cnname", 1003)
            System.objects.filter(id=id).update(sql_id=sql_id, enname=enname, cnname=cnname)
        return render(request, "member-list.html")


@csrf_exempt
def member_search(request):
    if request.method == "POST":
        name = request.POST.get("cnname", None)
        if name != None:
            result = list(System.objects.filter(cnname=name).all().values())
            print(result)
            # result = list(result)
            print(type(result), result)
            # a = [item for item in result]
            # return HttpResponse(result)
            return HttpResponse(json.dumps({'result': result}), content_type="application/json")
            # result = System.objects.filter(cnname=name).all()
            # return render(request, "search_result.html", {"list": result})
    # return render(request, "error.html")
