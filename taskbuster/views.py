# _*_ coding: utf-8 _*_

from django.shortcuts import render

def home(request):
    return render(request, "taskbuster/index.html", {})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
