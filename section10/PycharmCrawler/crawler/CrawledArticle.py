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