import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.quevidavideo.com/")
soup = BeautifulSoup(r.content, "html.parser")

find = soup.find_all("img")

for images in soup.find_all("img"):
  print images