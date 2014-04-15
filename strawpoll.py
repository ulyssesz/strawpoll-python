
import requests
import re


class StrawPoll(object):
	def __init__(self, data = None, url = None):

		self.url = None
		self.title = None
		self.results = {}
		self.totalVotes = None

		if url != None:
			self.url = url
			self.updateResults()

		elif data != None:
			r = requests.post('http://strawpoll.me/ajax/new-poll', data = data)
			if r.status_code == requests.codes.ok:
				self.url = "http://strawpoll.me/%s" % r.json()["id"]
				self.updateResults()
			else:
				self.url = None
		


	@classmethod
	def fromID(cls, id):
		return cls(url = "http://strawpoll.me/%s" % str(id))

	@classmethod
	def fromURL(cls, url):
		return cls(url = url.strip('/'))

	@classmethod
	def new(cls, title, options, multi = False, permissive = False):
		return cls(data = {"title":title, "options[]":options, "multi":True, "permissive":True})
	

	def updateResults(self):
		if self.url != None:
			r = requests.get("%s/r" % self.url)
			if r.status_code != requests.codes.ok: return
			
			content = r.content
			# Options
			matches = re.findall('<div class="pollOptionName">(.+?)</div>.+?<span>(.*?) vote[s]*</span>', content, flags = re.DOTALL)
			if matches != None:
				self.results = {k:int(v) for k,v in matches}
			else:
				self.results = {}


			# Title
			self.title = re.search('<div id="pollHeader">.+?<div>(.+?)</div>', content, flags = re.DOTALL)
			if self.title != None: self.title = self.title.group(1).strip()

			# Total count
			self.totalVotes = re.search('<div id="pollTotalVotes">.+?<span>(.+?)</span>', content, flags = re.DOTALL)
			
			if self.totalVotes != None: self.totalVotes = int(self.totalVotes.group(1))

		


		

if __name__ == "__main__":
	# Example
	s = StrawPoll.new("test", [1,"@"])

	# Poll results
	print s.url

	print s.title

	print s.results

	print s.totalVotes

	# Update results
	s.updateResults()

	# StrawPoll from ID
	t = StrawPoll.fromID(1440977)
	print t.title
	print t.results
	print t.totalVotes

	# StrawPoll from URL
	v = StrawPoll.fromURL("http://strawpoll.me/1440977")
	print v.title
	print v.results
	print v.totalVotes
