import aiohttp
import flask
import logging
from config import conf as c

logging.basicConfig(level=logging.INFO)

class VRP(object):
	def __init__(self, url):
		self.url = url

	def solve(self, orders):
		if orders:
			# do something
			pass

	def check_status(self):
		# how do we want to check status?
		pass

	def pull_results(self, jobid):
		# how do we want to pull results
		pass


def main():
	logging.info('starting...')	


if __name__ == '__main__':
	main()
