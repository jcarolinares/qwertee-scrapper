# -*- coding: utf-8 -*-

'''

Created by Julián Caro Linares

jcarolinares@gmail:

CC-BY-SA

'''

from PIL import Image #Image manippulation library
import time
import subprocess
import math

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
		file=open(file_name+".jpg",'w')
		r = s.get(self.img_url)
		with open(file_name+".jpg", "wb") as code:
			code.write(r.content)
		self.img=Image.open(file_name+".jpg")
		# self.img.show()

def main():

	t_shirt_list=[]
	n_pages=10 #Each page means 20 images
	x_size=20
	y_size=10
	# x_size=math.trunc(screen_resolution[0]/t_shirt_list[0].img.getbbox()[2])
	# y_size=math.trunc(screen_resolution[1]/t_shirt_list[0].img.getbbox()[3])
	screen_resolution=(x_size*255,y_size*306)



	for n_page in range(n_pages):

		#Downloading the page and creating the BeautifulSoup object
		url="https://www.qwertee.com/shop?sort=date"+"&p="+str(n_page+1)
		print(n_page+1)
		r  = s.get(url)
		data = r.text
		soup = BeautifulSoup(data,"lxml")

		#Scraping the info of the object and add the object to the object list
		for item in soup.find_all('li',class_="tee-list-item "):
			t_shirt=T_shirt(title=item.find('div',class_="inner").a.get_text(),author=item.find('span',class_="author").get_text().replace("by ",""),img_url=item.a.picture.img['src'])
			t_shirt.download_img()

			t_shirt_list.append(t_shirt)
	print("Tamaño objetos")
	print(len(t_shirt_list))


	wallpaper=Image.new("RGB",screen_resolution)
	# x_size=math.trunc(screen_resolution[0]/t_shirt_list[0].img.getbbox()[2])
	# y_size=math.trunc(screen_resolution[1]/t_shirt_list[0].img.getbbox()[3])



	print(x_size,y_size)

	total_index=0
	for v_index in range(y_size):
		#Horizontal paste
		for index in range(x_size):
			if total_index<len(t_shirt_list):
				#print("total_index: "+str(total_index)+"\n")
				wallpaper.paste(t_shirt_list[total_index].img, (255*index, 306 * v_index, 255+index*255, 306+306*v_index) )
				total_index=total_index+1
			# print(t_shirt_list[0].img.getbbox()[2])


	#wallpaper.show()
	# wallpaper.paste(img,(450*index,0))
	wallpaper.save('wallpaper.png','png')

	# Put the new screensaver
	subprocess.call('feh --bg-max ~/proyectos/qwertee-scrapper/wallpaper.png' ,shell=True)



# print(titles_url)

# #Images URL
# images_url=[]
# for link in soup.find_all('picture'):
# 	images_url.append(link.img['src'])
#     #print(link.get_text)
#     # print(link.img['src'])
#
# # print(images_url)
#
# #Pillow creates the wallpaper base image
# wallpaper=Image.new("RGB",(450*3,540*2))
# # wallpaper.show()
# wallpaper.save('wallpaper','png')
#
# #Download the three last t-shirts
# for index in range(6):
# 	# file=open(titles_url[index]+".jpg",'w')
# 	file=open("image_"+str(index)+".jpg",'w')
# 	r = s.get(images_url[index])
# 	with open("image_"+str(index)+".jpg", "wb") as code:
# 		code.write(r.content)
# 	img = Image.open("image_"+str(index)+".jpg")
# 	# img.show()
# 	if index <3:
# 		wallpaper.paste(img,(450*index,0))
# 	else:
# 		wallpaper.paste(img,(450*(index-3),540,450*(index-3)+450,2*540))#upper left corner, down right corner (x,y,x,y) #450,540,2*450,2*540)
#
# wallpaper.save('wallpaper.png','png')



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
#subprocess.call('feh --bg-max ~/proyectos/qwertee-scrapper/wallpaper.png' ,shell=True)


if __name__ == "__main__":
	s = requests.Session() #It creates a session to speed up the downloads
	main()
