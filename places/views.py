from django.shortcuts import render
from . models import Place
def test(request):
    temp=Place.objects.all()
    context={'place':temp}
    return render(request,'places/test.html',context)
def place(request,slug):
    p=Place.objects.get(slug=slug)
    context={"toy":p}
    return render(request,'places/place.html',context)
    
