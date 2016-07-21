from django.shortcuts import render
from main.models import Banner

# Create your views here.

def index(request):
	banner = Banner.objects.all()[0]
	response = {
		'banner': banner
	}
	return render (request, 'index.html', response)