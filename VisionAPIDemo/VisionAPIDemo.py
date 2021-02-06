import os, io
from google.cloud import vision_v1
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

client = vision_v1.ImageAnnotatorClient()

file_name = 'safety.jpg'
FOLDER_PATH = r'C:\Users\16477\OneDrive\Desktop\VisionAPIDemo\Images\Text'

with io.open(FOLDER_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision_v1.types.Image(content=content)

response = client.text_detection(image=image)
