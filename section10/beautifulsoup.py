import requests

r = requests.get("https://ibo.network/about")

print(r.status_code)
print(r.headers)
print(r.text)

from bs4 import BeautifulSoup
html = """
	<html>
		<body>
			<p class="something somethingElse">I'm a paragraph</p>
			<p>I am another paragraph</p>
		</body>
	</html>
"""

doc = BeautifulSoup(html, "html.parser")

print(doc)
for p in doc.find_all("p"):
	print(p.attrs)
	print(p.text) 