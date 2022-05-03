from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def farmercorner(request):
    return render(request, 'farmercorner.html')

def Buy(request):
    return render(request, 'Buy.html')

def Sell(request):
    return render(request, 'Sell.html')