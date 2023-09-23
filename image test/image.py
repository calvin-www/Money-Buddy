from PIL import Image
import pytesseract

im = Image.open(r'C:\Users\calvi\OneDrive\Desktop\github\HackRice13-Bot\imagetext02.jpg')

text = pytesseract.image_to_string(im)

print(text)