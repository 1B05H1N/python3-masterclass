"""
The Requests module 

In this lesson you will learn how to download a web page and view the HTML code of that website. 

For this we use the requests module (https://docs.python-requests.org/en/master/).
"""

import requests

r = requests.get("https://ibo.network/about")

print(r.status_code)
print(r.headers)
print(r.text)