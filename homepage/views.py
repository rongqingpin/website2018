from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def highlights(request):
	return render(request, 'homepage.html')