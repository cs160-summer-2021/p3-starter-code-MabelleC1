from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def home(request):
    return render(request, 'coloring/home.html')

def drawing(request):
    return render(request, 'coloring/drawing.html')

def templates(request):
    return render(request, 'coloring/templates.html')

def open(request):
    return render(request, 'coloring/open.html')

def animals(request):
	return render(request, 'coloring/animals.html')

def error(request):
	return render(request, 'coloring/error.html')