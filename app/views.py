from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10,'b':200,'c':30}
    return render(request,'conditions.html',d)


def loop(request):
    d={'name':'MESSI'}
    return render(request,'loop.html',d)