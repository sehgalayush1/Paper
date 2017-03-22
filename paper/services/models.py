from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Story(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True)
	url = models.CharField(max_length=2000, null=True, blank=True)
	code = models.CharField(max_length=225, null=True, blank=True)
	timestamp = models.DateTimeField(default=timezone.now)
	comments = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

	def build_url(self):
		self.url = u'www.reddit.com/{}'.format(self.code)
		return self.url
