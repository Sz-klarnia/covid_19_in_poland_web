
import requests
import time
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from .populate_db import *
from .models import Mobility
import io


def check_for_new_data():
    """Checks for new updates in google spreadsheet by looking for notifications on gmail. If there is new data, runs populate db function
    """
    SCOPES = ['https://mail.google.com/']
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('creds_4.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    stamp = int(time.time()) - 3600
    # Call the Gmail API
    results = service.users().messages().list(userId='me',q=f"from:notify@google.com after:{stamp}").execute()
    if results["resultSizeEstimate"] > 0:
        populate_database()

def get_new_modelling_data():
    """
    Getting up to date modelling data from websites and combining it into one database table
    """
    # get latest epidemic data from OWID 

    df = pd.read_json(requests.get("https://covid.ourworldindata.org/data/owid-covid-data.json").content)
    data = pd.DataFrame(df["POL"]["data"])

    # get latest government restriction data from Oxford tracker
    response = requests.get("https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_latest.csv").content
    rest = pd.read_csv(io.StringIO(response.decode('utf-8')))
    rest = rest[rest.CountryName == "Poland"]

    modelling = pd.DataFrame(Mobility.objects.values())
    prepare_model_data(data,rest,modelling)
    
    
