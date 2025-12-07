import os

AZURE_ENDPOINT = "https://ai-assessment-test-reso-resource.cognitiveservices.azure.com"
AZURE_KEY = "1svxfA9Ek0bUvyUztTbALQEL6bBmDg2BZTiHWBrOhVRJycSwTqdAJQQJ99BLACI8hq2XJ3w3AAAAACOG5dYU"

def load_env():
    os.environ["AZURE_OPENAI_API_KEY"] = AZURE_KEY
    os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_ENDPOINT
