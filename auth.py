
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials, BasicTokenAuthentication
from azure.identity import DefaultAzureCredential



def get_face_client_with_key(config):
  # Create an authenticated FaceClient using API Key
  endpoint = config['Authentication']['CognitiveFaceApiUrl']
  key = config['Authentication']['CognitiveFaceKey']
  return FaceClient(endpoint, CognitiveServicesCredentials(key))
  

def get_face_client_with_mi(config):
  # Create an authenticated FaceClient.
  endpoint = config['Authentication']['CognitiveFaceApiUrl']
  scope = config['Authentication']['FaceTokenCognitiveServicesEndpoint']
  
  creds = DefaultAzureCredential()
  access_token = creds.get_token(scope)
  #Convert to Dictionary
  dict_token = { "access_token": access_token.token}
  face_client = FaceClient(endpoint, BasicTokenAuthentication(dict_token))
  return face_client
  