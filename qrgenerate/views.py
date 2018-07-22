from django.shortcuts import render

# Create your views here.

def generate(request):
    user_id = "100nepal"
    return render(request,'qrgenerate.html',{'user_id':user_id})