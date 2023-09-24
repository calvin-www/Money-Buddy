import re
import pytesseract
from PIL import Image, ImageOps
import urllib.request






"""
# This bit of code is a little stupid an isn't necessary
def silly_error(image):
    try:
        text = pytesseract.image_to_string(image,config='--psm 4')
    except:
        silly_error(image)
    return text
"""

def read_receipt_url(url):

 
    # Open the image file
    urllib.request.urlretrieve(url, "receipt.png")
    image = Image.open("receipt.png")
    
    image = ImageOps.exif_transpose(image)
    # image.show()
    # Perform OCR using PyTesseract
    text = pytesseract.image_to_string(image,config='--psm 4')
    # text=silly_error(image)
    return text


def read_receipt(image_name):

 
    # Open the image file
    image = Image.open(r'/Users/eitfe/Vs_Code/Hackathon/' +image_name)
    
    image = ImageOps.exif_transpose(image)
    # image.show()
    # Perform OCR using PyTesseract
    text = pytesseract.image_to_string(image,config='--psm 4')
    # text=silly_error(image)
    return text

# These are two images that work when I've downloaded them
# text=read_receipt('receipt_real.png')
# text=read_receipt('good_receipt.jpg')

# This illustrates that we can do it with a url from online
text=read_receipt_url('https://i.pinimg.com/550x/5d/02/c9/5d02c94582f07a3b07e60647723eadc3.jpg')






def find_total(text):
    short_text=text.replace('.','')
    best_text=short_text.lower()
    # print(best_text)
    char_num=best_text.rfind('total')+6
    prev_char=best_text[char_num-1]
    first_num=0
    num_dif=0
    while not num_dif:
        cur_char=best_text[char_num]
        if cur_char.isnumeric() and first_num==0:
            first_num=char_num
        if prev_char.isnumeric() and not cur_char.isnumeric():
            num_dif=1
        else:
            prev_char=cur_char
            char_num+=1
    total=best_text[first_num:char_num]
    total=total[0: -2] +'.' + total[-2] +total[-1]
    return total


def find_date(text):
    search_pattern1 = '/./'
    temp1=re.compile(search_pattern1)
    search_pattern2='/../'
    temp2=re.compile(search_pattern2)
    slashes1=temp1.search(text)
    slashes2=temp2.search(text)
    if not slashes2== None:
        slashes=slashes2
    elif not slashes1== None: 
        slashes=slashes1
    if 'slashes' in locals():
        space=' '
        space_before=text.rfind(space, slashes.span()[0]-6, slashes.span()[0])
        space_after=text.find(space, slashes.span()[1], slashes.span()[1]+6)
        if space_before==-1:
            space_before=slashes.span()[0]-6+re.search('\n',text[slashes.span()[0]-6: slashes.span()[0]]).span()[1]
        if space_after==-1:
            space_after=slashes.span()[1]+re.search('\n',text[slashes.span()[1]: slashes.span()[1]+6]).span()[0]
        date=text[space_before+1:space_after]
    else:
        date=None
    return date

total=find_total(text)
print(total)
date=find_date(text)
print(date)





    
    