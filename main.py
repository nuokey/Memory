from tkinter import *
import random
from random import randint as rnd
import os

root=Tk()
root.resizable(False, False)

screen = Canvas(root, width=800, height=720, bg='white')
screen.pack()

images = []
game = True

class Image():
	def __init__(self, x, y):
		self.is_opened = False
		self.x = x
		self.y = y
		self.texture = None

	def image_add(self, image):
		self.texture = image
		self.image = PhotoImage(file=self.texture)
		self.button = Button(root, command=self.open)
		self.button.place(x=self.x, y=self.y, width=100, height=150)

	def open(self):
		global game
		if game:
			self.is_opened = True
			self.sImage = screen.create_image(self.x + 50, self.y + 75, image = self.image)
			self.button.destroy()
			opened_images.append(self)
			if len(opened_images) == 2:
				if opened_images[0].texture == opened_images[1].texture:
					win_images.append(opened_images[0])
					win_images.append(opened_images[1])
				else:
					root.after(500, opened_images[0].close)
					root.after(500, opened_images[1].close)

				del opened_images[0]
				del opened_images[0]

			i = 0
			for y in images:
				for x in y:
					if x.is_opened:
						i += 1
			if i == 16:
				game = False

	def close(self):
		self.is_opened = False
		self.button = Button(root, command=self.open)
		self.button.place(x=self.x, y=self.y, width=100, height=150)

def generate():
	global images
	images = []
	for y in range(4):
		images.append([])
		for x in range(4):
			images[y].append(Image(50 + 200 * x, 10 + 170 * y))

	images_add()

def images_add():
	global images
	for i in range(8):
		for q in range(2):
			end = False
			while not end:
				now_image = images[rnd(0, 3)][rnd(0, 3)]
				if now_image.texture == None:
					now_image.image_add("image" + str(i+1) + ".png")
					end = True

opened_images = []
win_images = []

generate()

root.mainloop()
