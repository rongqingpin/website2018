from django.shortcuts import render

# Create your views here.
def algorithm(request):
	return render(request, 'algorithm.html')

def frequency(request):
	return render(request, 'frequency.html')

def statistical(request):
	return render(request, 'statistical.html')

def dimension(request):
	return render(request, 'dimension.html')

def cluster(request):
	return render(request, 'cluster.html')

def regression(request):
	return render(request, 'regression.html')

def classify(request):
	return render(request, 'classify.html')

def simulation(request):
	return render(request, 'simulation.html')

def data(request):
	return render(request, 'data.html')
