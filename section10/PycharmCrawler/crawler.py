import crawler
from .crawler.ArtcleFetcher import ArtcleFetcher

fetcher = ArtcleFetcher()

counter = 0
for article in fetcher.fetch():
	if counter == 10:
		break
	counter += 1
	print(article.emoji + " : " + article.title)