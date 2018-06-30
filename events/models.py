from django.db import models
from django.utils import timezone

# Create your models here.

def set_upload_path_for_location(instance, filename):
	return 'locations/{}'.format(filename)

class Location(models.Model):
	name = models.CharField(max_length=200)
	addressline2 = models.CharField(max_length=100,blank=True)
	addressline3 = models.CharField(max_length=100,blank=True)
	lattitude = models.FloatField(null=True,blank=True, help_text='Google maps cordinates of the place. <a href="https://support.google.com/maps/answer/18539?co=GENIE.Platform%3DAndroid&hl=en&oco=1" target=_blank style="font-size:120%">visit here for help</a> ')
	longitude = models.FloatField(null=True,blank=True, help_text='<a href="https://support.google.com/maps/answer/18539?co=GENIE.Platform%3DAndroid&hl=en&oco=1" target=_blank style="font-size:120%">visit here for help</a> on how to Get these values')
	image = models.ImageField(upload_to=set_upload_path_for_location, null=True)
	
	def __str__(self):
		return self.name
	
	
class Event(models.Model):
	name = models.CharField('Name Of Event',max_length=250)
	description = models.TextField()
	date = models.DateTimeField('Date and Time')
	location = models.ForeignKey(to=Location, on_delete=models.SET_NULL, null=True, blank=True)
	rate = models.CharField(max_length=200,help_text=' eg. $100 available at Koala, etc',default="Free")
	banner = models.ImageField(upload_to= 'eventbanner/', blank=True)
	
	def __str__(self):
		return str(self.date.date())+' '+self.name
		
	def is_upcoming(self):
		now = timezone.now()
		if self.date >= now:
			return True
		return False
		
	def is_recent(self):
		return not self.is_upcoming
		
	def already_registered(self, attendee):
		attendees = self.attendee_set.all()
		if attendee in attendees:
			return True
		return False
	
	
class Photo(models.Model):
	which_event = models.ForeignKey(to=Event,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='events_gallery/')
	caption = models.CharField(max_length=100)
	
	def __str__(self):
		if len(self.caption) > 40:
			return self.caption[:40]+'...'
		return self.caption
	
class Attendee(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
		
	def __eq__(self, other):
		return (self.email == other.email and self.id != other.id)
	
	

	