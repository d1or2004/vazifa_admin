from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def liblary(request):
    return render(request, 'library.html')
