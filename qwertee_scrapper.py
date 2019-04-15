# -*- coding: utf-8 -*-

'''

Created by Julián Caro Linares

jcarolinares@gmail.# COMBAK:

CC-BY-SA

'''

import requests
from bs4 import BeautifulSoup

s = requests.Session() #It creates a session to speed up the downloads


url="https://www.qwertee.com"

#Downloading the page
r  = s.get(url)
data = r.text
soup = BeautifulSoup(data,"lxml")

#print(soup.prettify())

#Titles  url
titles_url=[]
for title in soup.find_all('div',class_="title"):
	titles_url.append(title.div.span.get_text())
    #print(title.div.span.get_text())

# print(titles_url)

#Images URL
images_url=[]
for link in soup.find_all('picture'):
	images_url.append(link.img['src'])
    #print(link.get_text)
    # print(link.img['src'])

# print(images_url)

#Download the three last t-shirts
for index in range(3):
    file=open(titles_url[index]+".jpg",'w')

    r = s.get(images_url[index])

    with open(titles_url[index]+".jpg", "wb") as code:
        code.write(r.content)
