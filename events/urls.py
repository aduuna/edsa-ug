from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:event_id>/', views.detail, name='detail'),
	path('<int:event_id>/register/', views.register, name='register'),
	path('<int:event_id>/register/done/', views.done, name='done'),
]