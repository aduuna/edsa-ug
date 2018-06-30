from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Event
from .forms import EventRegisterForm
from django.utils import timezone
from django.urls import reverse


# Create your views here.

def index(request):
	now = timezone.now()
	upcoming_events = Event.objects.filter(date__gte=now).order_by('date')[:5]
	recent_events = Event.objects.filter(date__lt=now).order_by('-date')[:5]
	args = {
		'upcoming_events':upcoming_events,
		'recent_events':recent_events,
	}
	return render(request, 'events/index.html',args)

def detail(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	args = {'event':event}
	return render(request, 'events/detail.html', args)
	
def register(request, event_id):
	if request.method == 'POST':
		form = EventRegisterForm(request.POST)
		if form.is_valid():
			event = get_object_or_404(Event, pk=1)
			data = form.cleaned_data
			attendee = event.attendee_set.create(name=data['name'],email=data['email'])
			if event.already_registered(attendee):
				attendee.delete() 
				return render(request, 'events/registerform.html', {'form':form, 'event_id':event_id, 'error_message':'User Already Registered'})
			else:
				attendee.save()
				return HttpResponseRedirect(reverse('events:done', args=(event_id,)))
	else:
		form = EventRegisterForm()
	return render(request, 'events/registerform.html', {'form':form, 'event_id':event_id})
	
	
def done(request, event_id):
	return render(request, 'events/donepage.html')