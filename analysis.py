import firebase_admin
from firebase_admin import credentials, initialize_app
import pandas as pd

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)


