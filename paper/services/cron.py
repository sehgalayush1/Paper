from django_cron import CronJobBase, Schedule

from twisted.internet import task, reactor

from . import crawlers

class ScrapeData(CronJobBase):
	RUN_EVERY_MINS = 5

	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'services.scrape_data'

	def do(self):
		reddit = crawlers.RedditCrawler()
		print "Crawling..."
		reddit.update_top_stories()
		print "Success!!!"
