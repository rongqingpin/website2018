from django.shortcuts import render

# Create your views here.
def iosapps(request):
	return render(request, 'iosapps.html')

def minis(request):
	return render(request, 'minis.html')
