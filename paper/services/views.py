from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
	return render(request, 'index.html')


def reddit(request):
	service = Service.objects.get(name='Reddit')
	stories = service.stories.all().reverse()

	return render(request, 'reddit.html', {'stories': stories})


def inshorts(request):
	service = Service.objects.get(name='Inshorts')
	stories = service.stories.order_by('timestamp')

	return render(request, 'inshorts.html', {'stories': stories})
