from django.shortcuts import render

# Create your views here.
def h1(request):
    return render(request,'app1/h1.html')