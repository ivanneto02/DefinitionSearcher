from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
from dotenv import load_dotenv
load_dotenv()

import os

API_KEY = os.environ["API_KEY"] 
API_ID = os.environ["API_ID"]
API_BASEURL = os.environ["API_BASEURL"]