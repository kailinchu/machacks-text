import os, io
import main
from google.cloud import vision_v1
## import pandas as pd

##os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "ServiceAccountToken.json"

#client = vision_v1.ImageAnnotatorClient()
def text():
    client = vision_v1.ImageAnnotatorClient.from_service_account_json(r"VisionAPIDemo/ServiceAccountToken.json")

    #image_file = 'IMG_8230.JPG'
    image_file = main.file_name()
    image_file = "safety.jpg"
    FOLDER_PATH = r'VisionAPIDemo/Images/Text'
    FILE_PATH = os.path.join(FOLDER_PATH, image_file)

    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)
    # pylint: disable=no-member
    response = client.text_detection(image=image)
    docText = response.full_text_annotation.text
    return docText
