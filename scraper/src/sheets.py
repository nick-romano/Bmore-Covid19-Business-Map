import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
from .config import get_root_path



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = os.path.join(get_root_path(), 'credentials.json')

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '13WirtfPlWtnLJJs_5EAa0A79UJ72iGcvhthlF6KYAus'
SAMPLE_RANGE_NAME = 'Hampden!A1:E'

columns = ["Place", "Menu", "Hours", "DirectOrder", "ThirdParty", "Details"]


def create_client():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=creds)
    sheet_api_service = service.spreadsheets()
    return sheet_api_service


def get_sheets(sheet_api_service):
    result = sheet_api_service.get(spreadsheetId=SAMPLE_SPREADSHEET_ID).execute()
    sheets = result.get('sheets', [])
    return sheets


def get_neighborhood_data(sheet_api_service):
    spreadsheets = get_sheets(sheet_api_service)
    all_data = pd.DataFrame([])
    for sheet in spreadsheets:
        props = sheet['properties']
        name = props['title']
        range = f"{name}!A:F"
        result = sheet_api_service.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                           range=range, valueRenderOption='FORMULA').execute()
        values = result.get('values', [])
        # columns = values[0]
        rows = values[2:]
        try:
            df = pd.DataFrame.from_records(rows, columns=columns)
            df = df.assign(Neighborhood=name)
            all_data = pd.concat([all_data, df])
        except Exception as e:
            e

    # all_data = all_data.rename(columns={"TBD": "Place"})
    all_data = all_data.loc[~pd.isna(all_data.Place)]
    all_data.columns = all_data.columns.str.replace('%', '')
    all_data.Menu = all_data.Menu.str.replace(r'(?s)=HYPERLINK\("(.*?)","(.*?)"\)', r"\1", regex=True)
    all_data.ThirdParty = all_data.ThirdParty.str.replace(r'(?s)=HYPERLINK\("(.*?)","(.*?)"\)', r"\1", regex=True)
    all_data.DirectOrder = all_data.DirectOrder.str.replace(r'(?s)=HYPERLINK\("(.*?)","(.*?)"\)', r"\1", regex=True)
    all_data = all_data.reset_index(drop=True)
    return all_data
