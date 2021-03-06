""""wordy stock <search term>" to return a stock photo for your search term"""

from random import shuffle
import re
try:
    from urllib import quote
except ImportError:
    from urllib.request import quote

import requests
from bs4 import BeautifulSoup

def stock(searchterm):
    searchterm = quote(searchterm)
    url = "https://www.shutterstock.com/search?searchterm={0}".format(searchterm)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html5lib")
    images = [x['src'] for x in soup.select('.img-wrap img')][:10]
    shuffle(images)

    return 'https:' + images[0] if images else ""

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"wordy stock (.*)", text)
    if not match:
        return

    return stock(match[0].encode("utf8"))

on_bot_message = on_message
