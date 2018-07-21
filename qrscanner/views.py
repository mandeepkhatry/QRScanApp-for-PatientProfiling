from django.shortcuts import render

# Create your views here.

def scan(request):
    return render(request,'qrscan.html');