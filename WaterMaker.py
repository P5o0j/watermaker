from PIL import Image
import os
from time import sleep
from os import system, name


inp = r'D:\\Strony\\Produkty\\msc\\input'
out = r'D:\\Strony\\Produkty\\msc\\output'
wm = Image.open("D:\\Strony\\Produkty\\msc\\frame.png")

def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

def resize():
    for file in os.listdir(inp):
        f_img = inp+"/"+file
        img = Image.open(f_img)
        img = img.resize((1600,1600))
        img.save(f_img)
resize()
print("Resizing Images")
sleep(2)
clear()


def watermark():
    for file in os.listdir(inp):
        f_img = inp+"/"+file
        out_img = out+"/"+file
        img = Image.open(f_img)
        img.paste(wm, (0,0), mask=wm)
        #img.show()
        img.save(out_img)
watermark()
print("Adding Frame")
sleep(2)
clear()


def cleanup():
    for file in os.listdir(inp):
        f_img = inp+"/"+file
        os.remove(f_img)
cleanup()
print("Cleaning Up")
sleep(2)
clear()