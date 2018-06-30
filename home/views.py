from django.shortcuts import render
from django.utils import timezone

from news.models import Article
from events.models import Event
from .models import AlertMessage,WelcomeMessage


# Create your views here.

def index(request):
	welcome = WelcomeMessage.objects.all()
	alert = AlertMessage.objects.all()
	now = timezone.now()
	articles = Article.objects.filter(date__lte=now).order_by('-date')[:5]
	events = Event.objects.filter(date__gte=now).order_by('-date')[:3]
	args = {
		'welcome':welcome,
		'articles':articles,
		'events':events,
		'alert':alert,
	}
	return render(request, 'homepage.html', args)