import logging
from django.utils import timezone
from models import *
from . import wrappers


class RedditCrawler():
	def update_top_stories(self):
		client = wrappers.RedditClient()
		try:
			stories = client.get_front_page_stories()

			for data in stories:
				story_data = data['data']
				story, created = Story.objects.get_or_create(code=story_data.get('permalink'))

				if created:
					story.title = story_data.get('title')
					story.date = timezone.datetime.fromtimestamp(story_data.get('created_utc'), timezone.get_current_timezone())
					story.comments = story_data.get('num_comments', 0)
					story.build_url()
					story.save()

		except Exception, e:
			logging.error(e)

		print "Stories saved!"
