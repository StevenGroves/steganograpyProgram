Welcome to our CST 205 Steganography Project!

When you run the project2.py file, you will be prompted to either encrypt or decrypt something.
If you have nothing to decrypt, choose encrypt.

1. Encrypt
	Here you can choose to:
		Encrypt text into an image of your choice
		Encrypt an image into an image of your choice

	Text Into Image:
		First you will type in the text you want encrypted into the text box. 
		When you hit the "Submit text" button, you choose what image you want to act as the cover image.
		Then, the program saves your image as "withHiddenText.png"
	Image Into Image:
		When you hit the encrypt button, you will be prompted first for the cover image (image you want to be seen publicly), then for the secret image (image you want to hide)
		Then, the program creates an image called hidden.png in whatever directory you forked into

2. Decrypt
	Here you can choose to:
		Decrypt text from an encrypted image
		Decrypt an image from an encrypted image

	Text From Image:
		First, you choose an image that you know has a message in it.
		Then the program prints out that text.
	Image From Image:
		Choose an image that you know has another image hidden inside it.
		The program will print out the secret image.
		Keep in mind that the secret image will be recognizable, but will not be the same as when it was encrypted.

3. File Descriptions:

	Currently, this program allows the user to encrypt text or a photo into a photo. It also allows the user to decrypt text and a photo from an encrypted photo that was modified with this same program. There are some example image files to manipulate as an example. 

	1.jpg - This is the cover image we have used for the encrypted media.
	flower.jpg - This is an example image used to be encrypted into our cover image example.
			This file was found on the internet and is copyrighted by flowerspictures.org.
	withHiddenImg.png - This is the resulting image from encrypting flower.jpg into 1.jpg. This image
			may be decrypted to result in the secretImg.png image file.
	secretImg.png - This is the resulting decrypted image after decrypting withHiddenImg.png.
	withHiddenText.png - This image currently has an encrypted text message. This image file may be decrypted
			with this decryption program to uncover the secret message.
