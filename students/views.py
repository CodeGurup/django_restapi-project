from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    return HttpResponse("<h2>List of students will be displayed here.</h2>")