from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.
def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my project')

def now_date(request):
    if request.method == 'GET':
        return HttpResponse(f'now is {date.today()}')
def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby, user')