from django.shortcuts import render

# Create your views here.


def scan(request):
    if request.method =="POST" :
        print(request.POST.get('code'))
    return render(request,'qrscan.html');