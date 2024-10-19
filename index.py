import pytesseract
from PIL import Image

# Path to the Tesseract executable
# Only necessary if pytesseract does not automatically locate Tesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

# Load an image from a file
image = Image.open('nwuscreentshot.png')

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Print the text content found in the image
print("message_start")
print(text)
print("message_end")

