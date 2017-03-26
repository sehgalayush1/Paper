from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Service(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	url = models.URLField(max_length=100)

	def __unicode__(self):
		return self.name



class Story(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True)
	body = models.TextField(null=True, blank=True)
	url = models.CharField(max_length=2000, null=True, blank=True)
	code = models.CharField(max_length=225, null=True, blank=True)
	timestamp = models.DateTimeField(default=timezone.now)
	comments = models.IntegerField(default=0)
	service = models.ForeignKey(Service, related_name='stories', null=True)

	def __unicode__(self):
		return self.title

	def build_url(self):
		self.url = u'{0}/{1}'.format(self.service.url, self.code)
		return self.url
