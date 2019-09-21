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

# Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
# This key will serve all examples in this document.
KEY = '40d7ec73c0fd4de8b4d6b3e1e30b3c80'
img_filename = 'img2.jpeg'
img_data = None
PERSON_GROUP_ID = 'junta'
# Used for the Snapshot and Delete Person Group examples.
# TARGET_PERSON_GROUP_ID = str(uuid.uuid4()

with open(img_filename, 'rb') as f:
    img_data = f.read()
# Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
# This endpoint will be used in all examples in this quickstart.
ENDPOINT = 'https://eastus.api.cognitive.microsoft.com/'
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
# face_client.person_group.create(
    # person_group_id='junta', name='junta')
camp1= face_client.person_group_person.create(PERSON_GROUP_ID, "camp1")
test_images = [file for file in glob.glob('*.jpeg')]
print (test_images)
for image in test_images:
    w = open(image, 'r+b')
    faceid = face_client.person_group_person.add_face_from_stream(
        PERSON_GROUP_ID,camp1.person_id, w)
    print(faceid)

# print(face_client)
# single_face_image_url ='img2.jpeg'
# single_image_name = os.path.basename(single_face_image_url)
# detected_faces = face_client.face.detect_with_url(url=single_face_image_url)
# if not detected_faces:
#     raise Exception('No face detected from image {}'.format(single_image_name))

# # Display the detected face ID in the first single-face image.
# # Face IDs are used for comparison to faces (their IDs) detected in other images.
# print('Detected face ID from', single_image_name, ':')
# for face in detected_faces: print (face.face_id)
# print()
