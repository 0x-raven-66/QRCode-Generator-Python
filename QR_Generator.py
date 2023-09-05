import pyqrcode       #to make QR code
from PIL import Image # to display images
import os             # system command line

print("=>> script to convert Text/Links to QR image <<=")
# getting the link to convert from the user
text=input("Enter Text to convert :")

# convert the text to QR code
qr=pyqrcode.create(text)

# convert the QR code to image and save in cwd automaticly
qrpng=qr.png('myqr.png', scale = 8)

# getting the cwd wich the image had been saved in 
cwd=os.getcwd()

# display the image from the directory show() function
# f => place holder
# r => raw string to ignore escape characters 
Image.open(fr"{cwd}\myqr.png").show()



