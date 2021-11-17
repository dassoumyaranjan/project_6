from django.shortcuts import render

# Create your views here.
def h2(request):
    return render(request,'app2/h2.html')