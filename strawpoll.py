
import requests
import re


class StrawPoll(object):
	def __init__(self, title, options, multi = False, permissive = False):

		data = {"title":title, "options[]":options, "multi":True, "permissive":True}
		r = requests.post('http://strawpoll.me/ajax/new-poll', data = data)

		if r.status_code == requests.codes.ok:
			self.poll_url = "http://strawpoll.me/%s" % r.json()["id"]
		else:
			self.poll_url = None
		
		
	
	def getResults(self):
		if self.poll_url == None:
			return None

		r = requests.get("%s/r" % self.poll_url)
		content = r.content

		matches = re.findall('<div class="pollOptionName">(.+?)</div>.+?<span>(.*?) vote[s]*</span>', content, flags = re.DOTALL)
		if matches != None:
			return {k:int(v) for k,v in matches}
		else:
			return None

if __name__ == "__main__":
	# Example
	s = StrawPoll("test", [1,"@"])

	# Print poll url
	print s.poll_url

	# Get results
	print s.getResults()
