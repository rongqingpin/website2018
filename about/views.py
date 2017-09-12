from django.shortcuts import render

# Create your views here.
def summary(request):
	return render(request, 'about.html')

def tutorial(request):
	return render(request, 'tutorial.html')

def catalog(request):
	return render(request, 'catalog.html')
