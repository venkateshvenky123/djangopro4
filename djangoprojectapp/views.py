from django.shortcuts import render
from django.http import HttpResponse
def hydjobsinfo(request):
    s='hyd jobs information'
    return HttpResponse(s)
def mumbaijobsinfo(request):
    s='mumbai jobs information'
    return HttpResponse(s)
def noidajobsinfo(request):
    s='noida jobs information'
    return HttpResponse(s)
def punejobsinfo(request):
    s='pune jobs information'
    return HttpResponse(s)