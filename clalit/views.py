from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import ARule


def index(request):
    # rules = ARule.objects.all()
    # output = ', '.join([str(rule) for rule in rules])
    return render(request, 'clalit/index.html')


def detail(request):
    rules = ARule.objects.all()
    output = ', '.join([str(rule) for rule in rules])
    return HttpResponse("You're looking at question %s." % output)

