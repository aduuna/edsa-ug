from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
	path('', views.index, name='index'),
	path('<str:news_slug>/', views.detail, name='detail'),
	#path('', detail, name=''),
]