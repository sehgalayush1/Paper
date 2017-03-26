from django_cron import CronJobBase, Schedule

from . import crawlers

class RedditCron(CronJobBase):
	RUN_EVERY_MINS = 5

	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'services.redditcron'

	def do(self):
		reddit = crawlers.RedditCrawler()
		print "Crawling..."
		reddit.update_top_stories()
		print "Success!!!"


class InshortsCron(CronJobBase):
	RUN_EVERY_MINS = 1

	schedule = Schedule(run_every_mins=0)
	code = 'services.inshortscron'

	def do(self):
		inshorts = crawlers.InshortsCrawler()
		print "Crawling..."
		inshorts.update_top_stories()
		print "Success!!!"
