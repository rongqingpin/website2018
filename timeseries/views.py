from django.shortcuts import render

# Create your views here.
def introduce(request):
	return render(request, 'motivation.html')

def algorithm(request):
	return render(request, 'algorithm.html')

def visualize(request):
	return render(request, 'visualize.html')