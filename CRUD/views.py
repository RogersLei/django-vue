# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
from django.core import serializers
from django.utils import timezone


from crud.models import Books


def index(request):
    return HttpResponse("Hello, world. You're at the CRUD index.")

def search(request):
    content = request.GET['content']
    try:
        books = serializers.serialize("json",Books.objects.filter(book_name__contains=content))
        res = {
            "code": 200,
            "data": books
        }
        print(books)
    except Exception,e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

def create(request):
    print('create')
    obj = json.loads(request.body)
    name = obj['name']
    price = obj['price']
    try:
        book = Books(book_name=name, book_price=price, book_time=timezone.now())
        book.save()
        res = {
            "code": 200,
        }
    except Exception,e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

def read(request):
    print('read')
    try:
        res = {
            "code": 200,
            "data": serializers.serialize("json",Books.objects.filter())
        }
    except Exception,e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

def update(request):
    print('update')
    obj = json.loads(request.body)
    pid = obj['id']
    name = obj['name']
    price = obj['price']
    try:
        Books.objects.filter(id=pid).update(book_price=price, book_name=name)
        res = {
            "code": 200
        }
    except Exception,e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

def delete(request):
    print('delete')
    obj = json.loads(request.body)
    print(obj)
    pid = obj['id']
    try:
        Books.objects.filter(id=pid).delete()
        res = {
            "code": 200
        }
    except Exception,e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")