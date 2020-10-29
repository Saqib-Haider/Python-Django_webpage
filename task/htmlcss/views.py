from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'about.html')
def add(request):
    return render(request, 'join.html')
def regis(request):
    return render(request,'regis.html')
def main(request):
    return render(request, 'about.html')