from django.db import models

# Create your models here.

class WelcomeMessage(models.Model):
	text = models.TextField()
	
	def __str__(self):
		return self.text
	
class AlertMessage(WelcomeMessage):
	pass