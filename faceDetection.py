import os
import requests
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '40d7ec73c0fd4de8b4d6b3e1e30b3c80',
}
faceattributes=""
params = urllib.parse.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    'recognitionModel': 'recognition_01',
    'returnRecognitionModel': 'false',
    'detectionModel': 'detection_01',
})
# params = urllib.parse.urlencode({
#     # Request parameters
#     'returnFaceId': 'true',
#     'returnFaceLandmarks': 'false',
#     'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
#     'recognitionModel': 'recognition_01',
#     'returnRecognitionModel': 'false',
#     'detectionModel': 'detection_01',
# })
img_filename = 'img2.jpeg'
img_data=None

with open(img_filename, 'rb') as f:
    img_data = f.read()
# api_url = "https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?%s"%params

# r = requests.post(api_url,
# #                  params=params,
#                   headers=headers,
#                   data=img_data)
# print (r.json())
try:
    conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, img_data, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))