import requests 

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv

class CrawledArtcle():
	def __init__(self, title, emoji, content, image):
		self.title = title
		self.emoji = emoji
		self.content = content
		self.image = image

class ArtcleFetcher():
	def fetch(self):
		url = "http://python.beispiel.programmierenlernen.io/index.php"

		while url != "":
			print(url)
			time.sleep(1)
			r = requests.get(url)
			doc = BeautifulSoup(r.text, "html.parser")			
			
		
			for card in doc.select(".card"):
				title = card.select(".card-title span")[1].text
				emoji = card.select_one(".emoji").text
				content = card.select_one(".card-text").text
				image = urljoin(url, card.select_one("img").attrs["src"])
				print(image)
				yield CrawledArtcle(title, emoji, content, image)

			next_button = doc.select_one(".navigation .btn")
			if next_button:
				next_href = next_button.attrs["href"]
				next_href = urljoin(url, next_href)
				url = next_href
				print(next_href)
			else:
				url = " "


fetcher = ArtcleFetcher()
fetcher.fetch()

counter = 0
for article in fetcher.fetch():
	if counter == 10:
		break
	counter += 1
	print(article.emoji + " : " + article.title)
