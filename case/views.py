from django.shortcuts import render

# Create your views here.

def cases(request):
    return render(request,'./case/cases.html')
