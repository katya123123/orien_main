from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, 'index.html')
    
def stosa(request):
    return render(request, 'stosa.html')
    
def asialines(request):
    return render(request, 'asialines.html')
    
def bc_crm(request):
    return render(request, 'bc-crm.html')
    
def bc_mp(request):
    return render(request, 'bc-mp.html')
    
def caravan(request):
    return render(request, 'caravan.html')
    
def dega(request):
    return render(request, 'dega.html')
    
def macdoner(request):
    return render(request, 'macdoner.html')
    
def mac_mp(request):
    return render(request, 'macdoner-mp.html')
    
def thearch(request):
    return render(request, 'thearch.html')
