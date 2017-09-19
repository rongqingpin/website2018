from django.shortcuts import render

# Create your views here.
def iosapps(request):
	return render(request, 'iosapps.html')

def avas(request):
	return render(request, 'avas.html')

def minis(request):
	return render(request, 'minis.html')

def studentLoan(request):
	return render(request, 'minis_studentLoan.html')
