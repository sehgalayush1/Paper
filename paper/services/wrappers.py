import logging, json, requests

class AbstractBaseClient(object):
	def __init__(self):
		self.headers = { 'user-agent': 'paper/1.0' }



class RedditClient(AbstractBaseClient):
	def get_front_page_stories(self):
		r = None
		stories = list()

		try:
			r = requests.get('https://www.reddit.com/.json', headers=self.headers)
			result = r.json()
			stories = result['data']['children']
			count = 25

			while result['data']['after']:
				r = requests.get(u'https://www.reddit.com/.json?count={0}&after={1}'.format(count, result['data']['after']), headers=self.headers)
				result = r.json()
				stories.extend(result['data']['children'])
				count += 25

		except ValueError, e:
			logging.error(e)
			logging.error(r)

		print "Stories scrapped!"
		return stories
