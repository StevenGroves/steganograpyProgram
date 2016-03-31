from Tkinter import *
import tkFileDialog
from PIL import Image, ImageOps

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
	data.save("hidden.png")

root = Tk()

root.configure(bg = 'DodgerBlue4')
root.title("Encrypt or Decrypt")
root.geometry('{}x{}'.format(425, 300))

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
	frame.grid(row = 0, column = 0, sticky = 'news')

##############################################################
#f1 - 
Label(f1, 
		text = "Main Menu:\n\nWhat would you like to do?",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 60,
		padx = 80).pack()
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
		padx = 87).pack()
#encode button
encryptTextButton = Button(f2,
						text = 'Hide Text\nin a Photo',
						bg = 'azure',
						fg = 'turquoise4',
						width = 12,
						command = lambda:nextFrame(f1))
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
		text = "Decrypt Options:\n\n1. Decrypt Text\n2. Decrypt a Photo\n3. Decrypt Unknown Media",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 40,
		padx = 79).pack()
#decrypt text button
decryptTextButton = Button(f3,
						text = 'Text',
						bg = 'azure',
						fg = 'turquoise4',
						width = 7,
						command = lambda:nextFrame(f1))
decryptTextButton.pack(padx = 9, side = LEFT)

#decrypt photo button
decryptPhotoButton = Button(f3,
						text = 'Photo',
						bg = 'turquoise4',
						fg = 'azure',
						width = 7,
						command = lambda:nextFrame(f1))
decryptPhotoButton.pack(padx = 9, side = LEFT)

#decrypt unknown button
decryptUnknownButton = Button(f3,
						text = 'Unknown',
						bg = 'slateblue4',
						fg = 'antiquewhite1',
						width = 7,
						command = lambda:nextFrame(f1))
decryptUnknownButton.pack(padx = 9, side = LEFT)

#return to main menu button
mainMenuButton = Button(f3,
						text = 'Return to\nMain Menu',
						bg = 'LightCyan',
						fg = 'red3',
						width = 8,
						command = lambda:nextFrame(f1))
mainMenuButton.pack(padx = 10, side = LEFT)
#####################################################################
#f4 - Encrypt picture from picture
Label(f4,
		text = "Hide a Photo in a Photo\nFirst, pick the cover image\nThen, pick the secret image",
		fg = 'white',
		bg = 'DodgerBlue4',
		font = 'times 18 bold',
		pady = 40,
		padx = 79).pack()
#encrypt button
encryptButton = Button(f4,
						text = 'Encrypt',
						bg = 'azure',
						fg = 'turquoise4',
						width = 7,
						command = lambda:hideImage())
encryptButton.pack(padx = 9, side = LEFT)
#back button
backButton = Button(f4,
						text = 'Back',
						bg = 'azure',
						fg = 'turquoise4',
						width = 7,
						command = lambda:nextFrame(f2))
backButton.pack(padx = 9, side = LEFT)

nextFrame(f1)

mainloop()