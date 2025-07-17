from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
          return HttpResponse("Hello there!")
def working(request):
        return HttpResponse("This is working page")
def homepage(request):
        data={
                'title':'Home Page',
                'pdata':'Hello there'
        }
        return render(request,"index.html",data)