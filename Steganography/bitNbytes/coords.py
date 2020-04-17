from PIL import Image
from base64 import b64decode

current = Image.open("./diff.png")
pixels = current.load()

height = current.size;
Binary = b''
Flag = ''


for y in range(0,height[0]):

    #Decodes and prints flag
    if y == 417:
        print(str(b64decode(Flag)))
        break

    #Converts byte sized var Binary to character and adds to the final Flag
    if y % 8 == 0 and y != 0:
        Flag += chr(int(Binary, 2))
        Binary = b''
    
    #Checks coordinates to see if a colour is present then assigns 1 if true, else 0.
    if pixels[0,y] == 1:
        Binary += b'1'      
    else:
        Binary += b'0'

