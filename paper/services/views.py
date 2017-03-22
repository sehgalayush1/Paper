from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
	stories = Story.objects.order_by('-timestamp')
	return render(request, 'index.html', {'stories':stories})
