from django.shortcuts import render

from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status 

# Create your views here.
def start_game(request):
    