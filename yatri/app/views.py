# Create your views here.
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf, request
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from app.forms import VehicleAddForm
from .models import Todo as DB
from .models import Aadhar, Vehicle
from .serializers import TodoSerialzier, AadhaarSerializer, VehicleSerializer
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth import authenticate, get_user_model, login, logout


# Create your views here.
# class HomePageView(TemplateView):
#     # DB = "./the_database.db"
#
#
#
#
#
#     def get(self, request, **kwargs):
#         def get_all_users(json_str=False):
#             rows = DB.objects.all().values()
#             if json_str:
#                 return json.dumps([dict(ix) for ix in rows])  # CREATE JSON
#             return rows
#
#         print(get_all_users(json_str=True))
#         return HttpResponse(get_all_users(json_str=True))


class TodoList(APIView):
    def get(self, request):
        todo = DB.objects.all()
        serializer = TodoSerialzier(todo, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Vehicles(View):
    form_class = VehicleAddForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        context = {
            "form": form,
        }
        return render(request, 'vehicle.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(None)
        print("hi")
        context = {
            "form": form,
        }
        return render(request, 'vehicle.html', context)


class Aadhaarlist(APIView):
    def get(self, request):
        aadhaar = Aadhar.objects.all()
        serializer = AadhaarSerializer(aadhaar, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AadhaarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Vehiclelist(APIView):
    def get(self, request):
        vehicle = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicle, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


