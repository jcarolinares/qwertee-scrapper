# -*- coding: utf-8 -*-

'''

Created by Julián Caro Linares

jcarolinares@gmail:

CC-BY-SA

'''

from PIL import Image #Image manippulation library
import time
import subprocess

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

#Pillow creates the wallpaper base image
wallpaper=Image.new("RGB",(450*3,540*2))
# wallpaper.show()
wallpaper.save('wallpaper','png')

#Download the three last t-shirts
for index in range(6):
	# file=open(titles_url[index]+".jpg",'w')
	file=open("image_"+str(index)+".jpg",'w')
	r = s.get(images_url[index])
	with open("image_"+str(index)+".jpg", "wb") as code:
		code.write(r.content)
	img = Image.open("image_"+str(index)+".jpg")
	# img.show()
	if index <3:
		wallpaper.paste(img,(450*index,0))
	else:
		wallpaper.paste(img,(450*(index-3),540,450*(index-3)+450,2*540))#upper left corner, down right corner (x,y,x,y) #450,540,2*450,2*540)

wallpaper.save('wallpaper.png','png')



#Download all the available images t-shirts
# counter=1
# for url in images_url:
# 	file=open("image_"+str(counter)+".jpg",'w')
# 	r = s.get(url)
# 	with open("image_"+str(counter)+".jpg", "wb") as code:
# 		code.write(r.content)
# 	img = Image.open("image_"+str(counter)+".jpg")
# 	wallpaper.paste(img)
# 	wallpaper.save('wallpaper','png')
# 	counter=counter+1

#Put the new screensaver
subprocess.call('feh --bg-max ~/proyectos/qwertee-scrapper/wallpaper.png' ,shell=True)
