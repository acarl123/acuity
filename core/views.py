from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def create(request):
    return render(request, "new_patient.html")