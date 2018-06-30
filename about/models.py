from django.db import models
from datetime import date
# Create your models here.

def set_upload_path(instance, filename):
	return 'profiles/{0}'.format(filename)
	
	
class Position(models.Model):
	PR = 'PR'
	VP = 'VP'
	GS = 'GS'
	OS = 'OS'
	FS = 'FS'
	RO = 'RO'
	EC = 'EC'
	POSITION_CHOICES = [
		(PR, 'President'),
		(VP, 'Vice-President'),
		(GS, 'General Secretary'),
		(OS, 'Organizing Secretary'),
		(FS, 'Financial Secretary'),
		(RO, 'Public Relations'),
		(EC, 'Electoral Commisioner'),
	]
	in_office = models.DateField('Office Commencement', default=date(2018,8,1))
	position_name = models.CharField('Position held', max_length=2, choices=POSITION_CHOICES, unique_for_year='in_office')
	
	def get_full_name(self):
		for i in self.POSITION_CHOICES:
			if i[0] == self.position_name:
				full_name = i[1]
				break
		return str(self.in_office.year)+' '+full_name
	
	def __str__(self):
		return self.get_full_name()
		
	def __gt__(self, other):
		return self.in_office >= other.in_office
	
	
class Person(models.Model):
	name = models.CharField(max_length=200)
	position = models.OneToOneField(Position, on_delete=models.CASCADE, limit_choices_to={'person':None})
	course = models.CharField(max_length=200)
	comp_year = models.IntegerField('Year of Completion')
	email = models.EmailField(max_length=254)
	number = models.CharField(max_length=14)
	portfolio = models.TextField('brief description', default='No Bio Available')
	h = models.IntegerField(default=10, help_text='do not touch this')
	w = models.IntegerField(default=10, help_text='do not touch this')
	profile_pic = models.ImageField(upload_to=set_upload_path, height_field='h', width_field='w',max_length=100)
	
	def __str__(self):
		return self.name
		
	def get_full_number(self):
		full_number = '233' + self.number[-9:]
		return int(full_number)
	
	
	
	