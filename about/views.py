from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Person,Position
from datetime import date

# Create your views here.
def index(request):
	persons=Person.objects.order_by('-position')
	args = {'persons':persons}
	return render(request, 'about/index.html',args)

def detail(request, profile_id):
	person = get_object_or_404(Person, pk=profile_id)
	return render(request, 'about/detail.html', {'person':person})