from django.shortcuts import render
from main.models import Banner, Category, Shop

# Create your views here.

def index(request):
	banner = Banner.objects.all()[0]
	category = Category.objects.all()
	shop = Shop.objects.all()[0]
	response = {
		'banner': banner,
		'category': category,
		'shop': shop
	}
	return render (request, 'index.html', response)

def contact(request):

	return render (request, 'contact.html', {})