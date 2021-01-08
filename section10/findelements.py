"""
Find elements in HTML

In this lesson you will learn how to extract information from a html file. 

To do this we disassemble the html file with Beautiful Soup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
"""

# First we get our page, which we actually wanted to read...

import requests
#r = requests.get("https://ibo.network/about") #I used my own website as I felt uncomfortable going to the instructors website 

from bs4 import BeautifulSoup
from urllib.parse import urljoin


class CrawledArticle():
	def __init__(self, title, emoji, content, image):
		self.title = title
		self.emoji = emoji
		self.content = content
		self.image = image

class ArticleFetcher():
	def fetch(self):
		url = "https://ibo.network/about"
		r = requests.get("https://ibo.network/about")
		doc = BeautifulSoup(r.text, "html.parser")

		articles = []
		for card in doc.select(".card"):
			title = card.select(".card-title span")[1].text
			emoji = card.select_one = (".emoji").text	
			content = card.select_one(".card-text").text
			image = urljoin(url, card.select_one("img").attrs["src"]
			print(image)
			crawled = CrawledArticle(title, emoji, content, image)
			articles.append(crawled)

		return articles

fetcher = ArticleFetcher()
fetcher.fetch()

"""articles = []

for card in doc.select(".card"):
	title = card.select(".card-title span")[1].text
	emoji = card.select_one = (".emoji").text	
	content = card.select_one(".card-text").text
	image = card.select_one("img").attrs["src"]

	crawled = CrawledArticle(title, emoji, content, image)
	articles.append(crawled)

for article in articles:
	print(article.title)
"""
"""	print(image)
	print(title)
	print(emoji)
	print(content)"""



