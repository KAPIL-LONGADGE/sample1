from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
def date_time_view(request, retun=None):
    date=datetime.datetime.now()
    s='<h1> The current Data And Time at server is :' +str(date)+'</h1>'
    return HttpResponse(s)