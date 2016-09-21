from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def index(request):
	latest_pizza_list = Pizza.objects.order_by('-nev')[:10]
	context = {
		'latest_pizza_list': latest_pizza_list,
	}
	return render(request, 'boti/index.html', context)
	
