from django.shortcuts import render

# Create your views here.
def algorithm(request):
	return render(request, 'algorithm.html')

def algo_intro(request):
	return render(request, 'algo_motivation.html')

def algo_tech(request):
	return render(request, 'algo_techniques.html')

def algo_resl(request):
	return render(request, 'algo_outcome.html')

def visualize(request):
	return render(request, 'visualize.html')

def vis_intro(request):
	return render(request, 'vis_motivation.html')

def vis_tech(request):
	return render(request, 'vis_techniques.html')

def vis_resl(request):
	return render(request, 'vis_outcome.html')