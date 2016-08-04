from django.shortcuts import render
from main.models import Banner, Category, Shop, Item

# Create your views here.

def index(request):
	banners = Banner.objects.all()
	categories = Category.objects.all()
	shop = Shop.objects.all()[0]
	response = {
		'banners': banners,
		'categories': categories,
		'shop': shop
	}
	return render (request, 'index.html', response)


def contact(request):
	return render (request, 'contact.html', {})


def about(request):
	return render (request, 'about.html', {})


def teckels(request, category_slug, category_id):
	teckels = Item.objects.filter(category_id=category_id)
	shop = Shop.objects.all()[0]
	response = {
		'teckels': teckels,
		'shop': shop
	}
	return render (request, 'teckels.html', response)

def teckel(request, item_slug, item_id):
	teckel = Item.objects.get(pk=item_id)
	shop = Shop.objects.all()[0]
	response = {
		'teckel': teckel,
		'shop': shop
	}
	return render (request, 'teckel.html', response)