from django.db import models

from datetime import date
import re
from bs4 import BeautifulSoup
# Create your models here.

def set_path(object, filename):
	today = date.today()
	return 'news/{}/{}'.format(today, filename)


class Article(models.Model):
	title = models.CharField('Title of Article',max_length=512)
	date = models.DateTimeField(auto_now=True)
	header = models.ImageField('Header Picture of Article', upload_to=set_path)
	body = models.TextField()
	views = models.IntegerField(default=0)
	slug = models.CharField(max_length=520, unique=True)
	
	def __str__(self):
		return self.title
	
	def shorten_body(self):
		soup = BeautifulSoup(self.body)
		text = soup.get_text(separator="... ")
		return text[:256]+'...'
		
	def cleaned_body(self):
		body = re.sub(r'''<img.*?(src=['"].*?['"]).*?>''', r'<img class="img-fluid" \1>', self.body)
		return body