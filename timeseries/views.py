from django.shortcuts import render

# Create your views here.
def acoustic(request):
	return render(request, 'acoustic.html')

def acoustic_intro(request):
	return render(request, 'acoustic_motivation.html')

# def acoustic_tech(request):
# 	return render(request, 'acoustic_techniques.html')

def acoustic_resl(request):
	return render(request, 'acoustic_outcome.html')

def supersonic(request):
	return render(request, 'supersonic.html')

def supersonic_intro(request):
	return render(request, 'supersonic_motivation.html')
