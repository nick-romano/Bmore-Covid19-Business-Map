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


def create_sheets_api_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=creds)
    sheet_api_service = service.spreadsheets()
    return sheet_api_service

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()


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
                           range=range).execute()
        values = result.get('values', [])
        columns = values[0]
        rows = values[2:]
        try:
            df = pd.DataFrame.from_records(rows, columns=columns)
            df = df.assign(Neighborhood=name)
            all_data = pd.concat([all_data, df])
        except Exception as e:
            e

    all_data = all_data.rename(columns={"TBD": "Place"})
    all_data = all_data.loc[~pd.isna(all_data.Place)]
    all_data

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))


if __name__ == '__main__':
    main()