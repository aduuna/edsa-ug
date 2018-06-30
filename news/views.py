from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.utils import timezone

from .models import Article

def index(request):
	today = timezone.now()
	articles = Article.objects.filter(date__lte=today).order_by('-date')[:10]
	return render(request, 'news/index.html', {'articles':articles})
	
def detail(request, news_slug):
	article = get_object_or_404(Article, slug=news_slug)
	return render(request, 'news/detail.html', {'article':article})
	