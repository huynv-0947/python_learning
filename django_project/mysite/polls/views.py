from django.shortcuts import render
from django.http import HttpResponse
import pdb

def index(request):
  return HttpResponse("Hello Django! Here is index!")
