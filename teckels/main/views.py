from django.shortcuts import render
from main.models import Banner, Category, Shop

# Create your views here.

def index(request):
	banners = Banner.objects.all()
	category = Category.objects.all()
	shop = Shop.objects.all()[0]
	response = {
		'banners': banners,
		'category': category,
		'shop': shop
	}
	return render (request, 'index.html', response)


def contact(request):
	return render (request, 'contact.html', {})


def about(request):
	return render (request, 'about.html', {})


def teckel(request, item_slug, item_id):
	return render (request, 'teckel.html', {})