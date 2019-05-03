# -*- coding: utf-8 -*-

'''

Created by Julián Caro Linares

jcarolinares@gmail

CC-BY-SA

'''

from PIL import Image #Image manippulation library
import time
import subprocess
import math
import argparse
import os.path
import random

import requests
from bs4 import BeautifulSoup


class T_shirt():
	def __init__(self,title="",author="",img_url=""):
		self.title=title
		self.author=author
		self.img_url=img_url
		self.price=0 #Not used right now

	def download_img(self):
		file_name=self.title.replace(" ","_").replace("\'","").lower() #We replace the spaces with underscores, remove the ' and convert the name to lowecase
		if not os.path.exists(img_path+file_name+".jpg"):
			print("Downloading "+file_name+".jpg")
			file=open(img_path+file_name+".jpg",'w')
			r = s.get(self.img_url)
			with open(img_path+file_name+".jpg", "wb") as code:
				code.write(r.content)
		else:
			print(img_path+file_name+".jpg"+" already downloaded")

		self.img=Image.open(img_path+file_name+".jpg")
		# self.img.show()

def main():

	t_shirt_list=[]
	n_pages=args.pages #Each page means 20 images
	x_size=args.cols
	y_size=args.rows

	# #Screen size cal alternative
	# x_size=math.trunc(screen_resolution[0]/t_shirt_list[0].img.getbbox()[2])
	# y_size=math.trunc(screen_resolution[1]/t_shirt_list[0].img.getbbox()[3])

	print("\nDownloading images from: ")
	for n_page in range(n_pages):

		#Downloading the page and creating the BeautifulSoup object
		url="https://www.qwertee.com/shop?sort=date"+"&p="+str(n_page+1)
		print("\n"+url)
		# print(n_page+1)
		r  = s.get(url)
		data = r.text
		soup = BeautifulSoup(data,"lxml")

		#Scraping the info of the object and add the object to the object list
		for item in soup.find_all('li',class_="tee-list-item"): #be careful with the additional space in the html code
			t_shirt=T_shirt(title=item.find('div',class_="inner").a.get_text(),author=item.find('span',class_="author").get_text().replace("by ",""),img_url=item.a.picture.img['src'])
			t_shirt.download_img()
			t_shirt_list.append(t_shirt)
	print("\nNumber of images: "+str(len(t_shirt_list)))

	#Building the wallpaper collage
	img_x=t_shirt_list[0].img.getbbox()[2]
	img_y=t_shirt_list[0].img.getbbox()[3]

	screen_resolution=(x_size*img_x,y_size*img_y)
	wallpaper=Image.new("RGB",screen_resolution)

	#Random argument active?
	if args.random==True:
		print("\nRandomizing images...")
		random.shuffle(t_shirt_list)

	total_index=0
	#Vertical paste
	for v_index in range(y_size):
		#Horizontal paste
		for index in range(x_size):
			if total_index<len(t_shirt_list):
				#print("total_index: "+str(total_index)+"\n")
				wallpaper.paste(t_shirt_list[total_index].img, (img_x*index, img_y * v_index, img_x+index*img_x, img_y+img_y*v_index) )
				total_index=total_index+1
			# print(t_shirt_list[0].img.getbbox()[2])

	#wallpaper.show()
	wallpaper.save('wallpaper.png','png')
	print("\nWallpaper created!")


	# Put the new screensaver
	subprocess.call('feh --bg-max ./wallpaper.png' ,shell=True)
	print("\nWallpaper ready!")

if __name__ == "__main__":

	#Initial folder setup
	img_path = "./img/"
	if not os.path.exists(img_path):
	    os.makedirs(img_path)

	s = requests.Session() #It creates a session to speed up the downloads

	#Cli arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("--pages", type=int, default=1,
		help="Defines the number of pages to be downloaded. Each page means 20 images")

	parser.add_argument("--rows", type=int, default=4,
		help="Defines the number of rows.")

	parser.add_argument("--cols", type=int, default=5,
		help="Defines the number of columns.")

	parser.add_argument("--random", type=bool,  default=False,
		help="Randomize the images used in the wallpaper->true/false")

	args = parser.parse_args()

	main()
