'''Team #44, Steganogasaurus
Members: Giselle Beltran
		 Raquel Figueroa 
		 Steven Groves
		 Brian Little
'''

from Tkinter import *
import tkFileDialog
from PIL import Image, ImageOps
import tkMessageBox

def nextFrame(frame):
	frame.tkraise()

def coverimage():
	filename = tkFileDialog.askopenfilename()
	return filename

def secretimage():
	filename = tkFileDialog.askopenfilename()
	return filename

def hideImage(s = 4):
	data = Image.open(coverimage())
	key = ImageOps.autocontrast(Image.open(secretimage()).resize(data.size))
	for x in range(data.size[0]):
		for y in range(data.size[1]):
			p = data.getpixel((x,y))
			q = key.getpixel((x,y))
			red = p[0] - (p[0] % s) + (s * q[0] / 255)
			green = p[1] - (p[1] % s) + (s * q[1] / 255)
			blue = p[2] - (p[2] % s) + (s * q[2] / 255)
			data.putpixel((x,y), (red, green, blue))
	data.save("withHiddenImg.png")
	data.show()
	nextFrame(f7)

def extract_image(from_image, s=4):
	hiddenImg = Image.open(from_image)
	for x in range(hiddenImg.size[0]):
		for y in range(hiddenImg.size[1]):
			p = hiddenImg.getpixel((x,y))
			red = (p[0] % s) * 255 / s
			green = (p[1] % s) * 255 / s
			blue = (p[2] % s) * 255 / s
			hiddenImg.putpixel((x,y), (red, green, blue))
	#return data
	hiddenImg.save("secretImg.png")
	hiddenImg.show()
	nextFrame(f11)


#Used this website for reference on encoding strings into images: 
#https://www.daniweb.com/programming/software-development/code/485063/hide-private-message-in-an-image-python
	
def hideString():
	data = e.get()
	datalength = len(data)
	image = Image.open(coverimage())
	height, width = image.size
	newimg = image.copy()
	
	count = 0
	for x in range(0, height):
		for y in range(0, width):
			red, green, blue = newimg.getpixel((x, y))
			if x ==0 and y == 0:
				new_val = datalength #Very first red pixel will hold the value of the length of the string
			elif count <= datalength:
				temp = data[count - 1]
				new_val = ord(temp) + 3 #the +3 is just to make it less obvious to decrypt
			else:
				new_val = red
			newimg.putpixel((x, y), (new_val, green, blue))
			count += 1
	newimg.save("withHiddenText.png")
	newimg.show()
	nextFrame(f6)
			
def decodeString():
	image = Image.open(coverimage())
	height, width = image.size

	msg = ""
	count = 0
	for x in range(0, height):
		for y in range(0, width):
			red, green, blue = image.getpixel((x, y))
			if x == 0 and y == 0: #We assume the first red value holds the length of the string we're decoding
				length = red
			elif count <= length:
				msg += unichr(red - 3) #-3 to put the value back to original state
			if count > length:
				print "Secret Message: " + msg
				nextFrame(f9)
				return msg
			count += 1
			

root = Tk()

root.configure(bg = 'DodgerBlue4')
root.title("Encrypt or Decrypt")
root.geometry('{}x{}'.format(460, 300))

f1 = Frame(root) # Main menu
f2 = Frame(root) # Encrypt menu
f3 = Frame(root) # Decrypt menu
f4 = Frame(root) # Encrypt photo
f5 = Frame(root) # Encrypt text
f6 = Frame(root) # successful text encrypted
f7 = Frame(root) # successful photo encrypted
f8 = Frame(root) # Decrypt text from photo
f9 = Frame(root) # Successful text decryption
f10 = Frame(root) # Decrypt photo from photo
f11 = Frame(root) # Successful photo decryption


for frame in (f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11):
	frame.grid(row = 0, column = 0, sticky = 'news')

##############################################################
#f1 - 
Label(f1, 
		text = "Main Menu:\n\nWhat would you like to do?",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 60,
		padx = 100).pack()
#encode button
encodebutton = Button(f1,
						text = 'Encrypt',
						bg = 'azure',
						fg = 'turquoise4',
						width = 13,
						command = lambda:nextFrame(f2))
encodebutton.pack(padx = 35, side = LEFT)

#decode button
decodebutton = Button(f1,
						text = 'Decrypt',
						bg = 'turquoise4',
						fg = 'azure',
						width = 13,
						command = lambda:nextFrame(f3))
decodebutton.pack(padx = 50, side = RIGHT)
########################################################################
#f2 -Encrypt
Label(f2, 
		text = "Encrypt Options:\n\n1. Hide Text in a Photo\n2. Hide a Photo in a Photo",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 50,
		padx = 105).pack()
#encode button
encryptTextButton = Button(f2,
						text = 'Hide Text\nin a Photo',
						bg = 'azure',
						fg = 'turquoise4',
						width = 12,
						command = lambda:nextFrame(f5))
encryptTextButton.pack(padx = 10, side = LEFT)

#decode button
encryptPhotoButton = Button(f2,
						text = 'Hide a Photo\nin a Photo',
						bg = 'turquoise4',
						fg = 'azure',
						width = 12,
						command = lambda:nextFrame(f4))
encryptPhotoButton.pack(padx = 10, side = LEFT)

#return to main menu button
mainMenuButton = Button(f2,
						text = 'Return to\nMain Menu',
						bg = 'LightCyan',
						fg = 'red3',
						width = 12,
						command = lambda:nextFrame(f1))
mainMenuButton.pack(padx = 10, side = LEFT)
#######################################################################
#f3 - Decrypt
Label(f3, 
		text = "Decrypt Options:\n\n1. Decrypt Text\n2. Decrypt a Photo",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 40,
		padx = 100).pack()
#decrypt text button
decryptTextButton = Button(f3,
						text = 'Text',
						bg = 'azure',
						fg = 'turquoise4',
						width = 7,
						command = lambda:nextFrame(f8))
decryptTextButton.pack(padx = 30, side = LEFT)

#decrypt photo button
decryptPhotoButton = Button(f3,
						text = 'Photo',
						bg = 'turquoise4',
						fg = 'azure',
						width = 7,
						command = lambda:nextFrame(f10))
decryptPhotoButton.pack(padx = 30, side = LEFT)

#return to main menu button
mainMenuButton = Button(f3,
						text = 'Return to\nMain Menu',
						bg = 'LightCyan',
						fg = 'red3',
						width = 8,
						command = lambda:nextFrame(f1))
mainMenuButton.pack(padx = 30, side = LEFT)
#####################################################################
#f4 - Encrypt picture into picture
Label(f4,
		text = "Hide a Photo in a Photo\nFirst, pick the cover image\nThen, pick the secret image",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 75,
		padx = 100).pack()
#encrypt button
encryptButton = Button(f4,
						text = 'Encrypt',
						bg = 'turquoise4',
						fg = 'azure',
						width = 7,
						command = lambda:hideImage())
encryptButton.pack(padx = 70, side = LEFT)
#back button
backButton = Button(f4,
						text = 'Back',
						bg = 'azure',
						fg = 'turquoise4',
						width = 7,
						command = lambda:nextFrame(f2))
backButton.pack(padx = 70, side = RIGHT)

#######################################################################
#Frame 5 - Hide Text in a Photo
Label(f5,
		text = 'Enter the text you\n would like to encode:',
		font = 'times 20 bold',
		bg = 'DodgerBlue4',
		fg = 'white',
		pady = 70,
		padx = 120).pack()

#Text box		
e = Entry(f5, bd = 5)
e.pack()
	
encryptStringButton = Button(f5,
						text ='Submit\nText',
						bg = 'turquoise4',
						fg = 'azure',
						width = 8,
						command = lambda:hideString())
encryptStringButton.pack(padx = 50, side = LEFT)
		
mainMenuButton = Button(f5,
						text = 'Return to\nMain Menu',
						bg = 'LightCyan',
						fg = 'red3',
						width = 12,
						command = lambda:nextFrame(f1))
mainMenuButton.pack(padx = 70, side = RIGHT)
#######################################################################
#f6 - Show successful text encrypting
Label(f6, 
		text = "Text Successfully\nEncrypted in Photo.\nFile in Directory.",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 60,
		padx = 95).pack()

mainMenuButton = Button(f6,
						text = 'Return to\nMain Menu',
						bg = 'LightCyan',
						fg = 'red3',
						width = 12,
						command = lambda:nextFrame(f1))
mainMenuButton.pack(padx = 10, side = LEFT)

quitbutton = Button(f6,
						text = 'Quit',
						bg = 'turquoise4',
						fg = 'azure',
						width = 13,
						command = lambda:root.quit())
quitbutton.pack(padx = 50, side = RIGHT)
########################################################################
#f7 - Show successful photo encrypting
Label(f7, 
		text = "Photo successfully\nencrypted in photo.\nFile in directory.",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 80,
		padx = 100).pack()

mainMenuButton = Button(f7,
						text = 'Return to\nMain Menu',
						bg = 'LightCyan',
						fg = 'red3',
						width = 12,
						command = lambda:nextFrame(f1))
mainMenuButton.pack(padx = 50, side = LEFT)

quitbutton = Button(f7,
						text = 'Quit',
						bg = 'turquoise4',
						fg = 'azure',
						width = 13,
						command = lambda:root.quit())
quitbutton.pack(padx = 50, side = RIGHT)
########################################################################
#f8 - Decrypt text from a picture
Label(f8,
		text = "Decrypt Text From a Photo.\n Choose a File:",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 80,
		padx = 100).pack()
#Decrypt text from photo button
decryptTextImage = Button(f8,
						text = 'Choose Photo\nFrom a File',
						bg = 'turquoise4',
						fg = 'azure',
						width = 12,
						command = lambda:decodeString())
decryptTextImage.pack(padx = 50, side = LEFT)
#return to main menu button
mainMenuButton = Button(f8,
						text = 'Return to\nMain Menu',
						bg = 'LightCyan',
						fg = 'red3',
						width = 10,
						command = lambda:nextFrame(f1))
mainMenuButton.pack(padx = 50, side = LEFT)
#################################################################
#f9 - Show successful text decrypting
Label(f9, 
		text = "Text successfully\ndecrypted from photo.",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 90,
		padx = 110).pack()

mainMenuButton = Button(f9,
						text = 'Return to\nMain Menu',
						bg = 'LightCyan',
						fg = 'red3',
						width = 12,
						command = lambda:nextFrame(f1))
mainMenuButton.pack(padx = 10, side = LEFT)

quitbutton = Button(f9,
						text = 'Quit',
						bg = 'turquoise4',
						fg = 'azure',
						width = 13,
						command = lambda:root.quit())
quitbutton.pack(padx = 50, side = RIGHT)
########################################################################
#f10 - Decrypt photo from a picture
Label(f10,
		text = "Decrypt Photo From a Photo.\n Choose a File:",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 90,
		padx = 90).pack()
#Decrypt text from photo button
decryptTextImage = Button(f10,
						text = 'Choose Photo\nFrom a File',
						bg = 'turquoise4',
						fg = 'azure',
						width = 12,
						command = lambda:extract_image(coverimage()))
decryptTextImage.pack(padx = 50, side = LEFT)
#return to main menu button
mainMenuButton = Button(f10,
						text = 'Return to\nMain Menu',
						bg = 'LightCyan',
						fg = 'red3',
						width = 10,
						command = lambda:nextFrame(f1))
mainMenuButton.pack(padx = 50, side = LEFT)
#################################################################
#f11 - Show successful photo decrypting
Label(f11, 
		text = "Hidden photo successfully\ndecrypted from photo.",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 90,
		padx = 100).pack()

mainMenuButton = Button(f11,
						text = 'Return to\nMain Menu',
						bg = 'LightCyan',
						fg = 'red3',
						width = 12,
						command = lambda:nextFrame(f1))
mainMenuButton.pack(padx = 10, side = LEFT)

quitbutton = Button(f11,
						text = 'Quit',
						bg = 'turquoise4',
						fg = 'azure',
						width = 13,
						command = lambda:root.quit())
quitbutton.pack(padx = 50, side = RIGHT)
########################################################################


nextFrame(f1)

mainloop()
