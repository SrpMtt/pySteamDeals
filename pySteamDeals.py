import urllib.request
import requests
from bs4 import BeautifulSoup
  

def get_html(url):
   req = urllib.request.Request(url, headers={'User_Agent':'Mozilla/5.0'})
   return urllib.request.urlopen(req)


def list_titles(url):
   titles = []
   soup = BeautifulSoup(get_html(url))
   for link in soup.findAll('span'):
      if 'title' in str(link.get('class')):
         game_title = str(link)
         titles.append(game_title[20:-7])
   return titles


def list_discounts(url):
   discounts = []
   soup = BeautifulSoup(get_html(url))
   for link in soup.findAll('div'):
      if 'search_discount' in str(link.get('class')):
         game_discount = str(link)
         discounts.append(''.join(c for c in game_discount if c in '-%0123456789'))
   return discounts


def list_price(url):
   soup = BeautifulSoup(get_html(url))
   for link in soup.findAll('br'):
      if '€' in str(link):
         game_price = str(link)
         print(str(link))


def get_links():
   base_url = 'http://store.steampowered.com/search/?specials=1&os=win#sort_by=_ASC&os=win%2Cmac%2Clinux&specials=1&page=1'
   links = [base_url]
   soup = BeautifulSoup(get_html(base_url))
   for link in soup.findAll('a'):
      if 'SearchLinkClick' in str(link.get('onclick')):
         href = str(link.get('href'))
         links.append(href)
   return links[:-1]



for url in get_links():
   games = zip(list_titles(url), list_discounts(url))
   for title, discount in games:
      print(title, discount)