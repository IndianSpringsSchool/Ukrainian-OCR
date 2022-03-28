import numpy as np
from PIL import Image
from easyocr import Reader

def openImg():
   return np.invert(Image.open('image.jpg').convert('L')) 

def readText(filename):
   # Load model for Ukranian
   reader_uk = Reader(['uk'])

   # Read the data
   text = reader_uk.readtext(filename, detail = 0, paragraph = True)

   # Join texts writing each text in new line
   return '\n'.join(text)

# Reads a blocked text
print(readText('sample_text.jpg') + '\n')

# Reads a sample Ukrainian passport (the model messes up on the english and icons)
# print(readText('sample_passport.jpg'))