from django.shortcuts import render

# Create your views here.
def waves(request):
	return render(request, 'waves.html')

def wave_intro(request):
	return render(request, 'wave_motivation.html')

def wave_tech(request):
	return render(request, 'wave_techniques.html')

def wave_resl(request):
	return render(request, 'wave_outcome.html')