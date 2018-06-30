from django.urls import path
from . import views

app_name = 'about'
urlpatterns = [
	path('', views.index, name='index'),
	#path('profiles/', views.profiles, name='profiles'),
	path('profiles/<int:profile_id>/', views.detail, name='profile_detail')
]