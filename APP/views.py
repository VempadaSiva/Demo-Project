from django.shortcuts import render, redirect
from rest_framework import mixins
from .models import Form
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import responses, Response
from rest_framework import status
from .Serializer import Formserializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, routers, viewsets


def all(request):
    return render(request, 'Details.html')


def any(request):
    uid = request.POST.get('id')
    title = request.POST.get('title')
    des = request.POST.get('des')
    date = request.POST.get('date')
    datee = request.POST.get('datee')
    if uid == '':
        k = Form(title=title, des=des, date=date, datee=datee)
        k.save()
        return render(request, 'Details.html')
    else:
        k = Form.objects.filter(id=uid).update(title=title, des=des, date=date, datee=datee)
        return render(request, 'Details.html', {'k': k})


def data(request):
    data = Form.objects.all()
    return render(request, 'data.html', {'y': data})


def edit(request, id):
    edit = Form.objects.get(id=id)
    return render(request, 'Details.html', {'k': edit})


def delete(request, id):
    delete = Form.objects.get(id=id)
    delete.delete()
    return redirect(data)





class FormList(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = Formserializer


class FormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form.objects.all()
    serializer_class = Formserializer
    lookup_field = 'id'
