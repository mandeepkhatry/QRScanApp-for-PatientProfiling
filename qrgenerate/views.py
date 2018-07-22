from django.shortcuts import render

# Create your views here.

def generate(request):

    #Test user id
    #Use currently logged in user's userid
    user_id = "100nepal"
    return render(request,'qrgenerate.html',{'user_id':user_id})