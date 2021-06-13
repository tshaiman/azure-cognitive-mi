
import configparser
import os

from auth import get_face_client_with_key, get_face_client_with_mi


def get_config():
    config = configparser.ConfigParser()
    config.read("./config.ini")
    return config


# This Sample is taken from the Official Azure Documentation 
# https://docs.microsoft.com/en-us/azure/cognitive-services/face/quickstarts/client-libraries?tabs=visual-studio&pivots=programming-language-python#detect-faces-in-an-image

def detect_face(face_client):
  # Detect a face in an image that contains a single face
  single_face_image_url = 'https://www.biography.com/.image/t_share/MTQ1MzAyNzYzOTgxNTE0NTEz/john-f-kennedy---mini-biography.jpg'
  single_image_name = os.path.basename(single_face_image_url)
  # We use detection model 3 to get better performance.
  detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detection_model='detection_03')
  if not detected_faces:
      raise Exception('No face detected from image {}'.format(single_image_name))

  # Display the detected face ID in the first single-face image.
  # Face IDs are used for comparison to faces (their IDs) detected in other images.
  print('Detected face ID from', single_image_name, ':')
  for face in detected_faces: print (face.face_id)
  print()


print("face recognision demo with various authentication methods")
config = get_config()

#############################################################
#Part 1 : Authenticate to Cognitive Service API with a KEY 
#############################################################
client = get_face_client_with_key(config)
detect_face(client)

######################################################################
#Part 2 : Authenticate to Cognitive Service API with Managed Identity
######################################################################
#mi_client = get_face_client_with_mi(config)
#detect_face(mi_client)