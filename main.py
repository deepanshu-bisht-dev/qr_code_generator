# First we are going to install qrcode library by commanding the terminal as pip install qrcode

import qrcode

url = input("Enter your url : ")
file_name = input("Enter file name you want to save it as : ")

if not(file_name.endswith(".png")):
    file_name = file_name + ".png"

img = qrcode.make(url)
img.save(file_name)