import logging, json, requests
from bs4 import BeautifulSoup

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



class InshortsClient(AbstractBaseClient):
	def get_front_page_stories(self):
		r = None
		stories = list()

		try:
			r = requests.get('https://www.inshorts.com/en/read', headers=self.headers)
			soup = BeautifulSoup(r.text, 'html.parser')

			for story in soup.find_all('div', attrs={'class': 'news-card'}):
				title = story.find(itemprop="headline").string
				body = story.find(itemprop="articleBody").string
				result = {'title': title, 'body': body}
				stories.append(result)

		except ValueError, e:
			logging.error(e)
			logging.error(r)

		print "Stories scrapped!"
		return stories
