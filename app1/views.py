from django.shortcuts import render

# Create your views here.
def csk(request):
    return render(request,'dhoni.html')
def rcb(request):
    return render(request,'virat.html')