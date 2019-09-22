import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

class location():
    def __init__(self, face_ids, location):
        self.face_ids=face_ids
        self.location = location
def create_map(path,l):
    global mapphoto
    global face_client
    test_images = [file for file in glob.glob(path+'*.jpeg')]
    for image in test_images:
      w = open(image, 'r+b')
      faces = face_client.face.detect_with_stream(w)
      second_image_face_IDs = list(map(lambda x: x.face_id, faces))
      loc=location(second_image_face_IDs,l)
      mapphoto[image]=loc
    #   print (mapphoto)
def find_latest(path):
    location=None
    global face_client
    global mapphoto
    w = open(path, 'r+b')
    faces_1 = face_client.face.detect_with_stream(w)
    for face in faces_1:
      for key in mapphoto:
    #    print(mapphoto[key].face_ids)
       similar_faces=face_client.face.find_similar(face_id=face.face_id, face_ids=mapphoto[key].face_ids)
    if not similar_faces:
        l="kk"
    else:
       location=mapphoto[key].location
    #    print(location)
    if(location==None):
        print ("image Not found")
    else:    
        print(location) 
KEY = '40d7ec73c0fd4de8b4d6b3e1e30b3c80'
img_filename = 'img2.jpeg'
img_data = None
mapphoto={}
PERSON_GROUP_ID = 'junta'
ENDPOINT = 'https://eastus.api.cognitive.microsoft.com/'
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
create_map("./gainesville/","gainesville")
create_map("./miami/","miami")

create_map("./ram/","new york")

# find_latest("./harshit/check.jpg")
find_latest('./kunal/check.jpeg')
find_latest('./ram/check.jpeg')
find_latest('./noopur/check.jpeg')

