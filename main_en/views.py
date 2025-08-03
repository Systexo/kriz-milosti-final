# main_en/views.py
from django.shortcuts import render

def index(request):
    return render(request, "main_en/index.html")

def about(request):
    return render(request, "main_en/about.html")

def visit_us(request):
    return render(request, "main_en/visit-us.html")

def sermons(request):
    return render(request, "main_en/sermons.html")

def connect(request):
    return render(request, "main_en/connect.html")

def statement_of_faith(request):
    return render(request, "main_en/statement-of-faith.html")
