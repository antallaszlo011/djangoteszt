from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

def index(request):
	latest_person_list = Szemely.objects.order_by('-reg_dat')[:6]
	template = loader.get_template('profilok/index.html')
	context = {
		'latest_person_list': latest_person_list,
	}
	return HttpResponse(template.render(context, request))
	
def detail(request, szemely_id):
	szemely = Szemely.objects.get(id=szemely_id)
	context = {
		'szemely': szemely
	}
	return render(request, 'profilok/detail.html', context)
	
def delete(request, szemely_id):
	szemely_nev = Szemely.objects.get(id=szemely_id)
	szemely = Szemely.objects.get(id=szemely_id)
	szemely.delete()
	return HttpResponse("Sikeresen kitorolted %s-t." % szemely_nev)