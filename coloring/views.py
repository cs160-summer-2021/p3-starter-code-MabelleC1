from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def screen1(request):
    return render(request, 'coloring/screen1.html')

def createnew(request):
    return render(request, 'coloring/createnew.html')

def templates(request):
    return render(request, 'coloring/templates.html')

def open(request):
    return render(request, 'coloring/open.html')