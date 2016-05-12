import requests
from bs4 import BeautifulSoup

url = "http://www.quevidavideo.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

find = soup.find_all("img")

for images in find:
  print images