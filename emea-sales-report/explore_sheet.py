#!/usr/bin/env python3
"""Explore the Google Sheet structure using direct API calls."""

import json
import requests
from datetime import datetime, timedelta
import jwt
import time

# Configuration
CREDENTIALS_FILE = '/home/user/Demo/emea-sales-report/credentials.json'
SPREADSHEET_ID = '1-YOg_3uj_IYeY0HiWG_xtdYCDU1Qbjjzzwa_YOjoRNw'
SHEET_NAME = 'EMEA CQ Deal Updates'

def get_access_token():
    """Get OAuth2 access token using service account credentials."""
    with open(CREDENTIALS_FILE) as f:
        creds = json.load(f)

    # Create JWT
    now = int(time.time())
    payload = {
        'iss': creds['client_email'],
        'sub': creds['client_email'],
        'aud': 'https://oauth2.googleapis.com/token',
        'iat': now,
        'exp': now + 3600,
        'scope': 'https://www.googleapis.com/auth/spreadsheets.readonly https://www.googleapis.com/auth/drive.readonly'
    }

    # Sign JWT with private key
    signed_jwt = jwt.encode(payload, creds['private_key'], algorithm='RS256')

    # Exchange JWT for access token
    response = requests.post(
        'https://oauth2.googleapis.com/token',
        data={
            'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
            'assertion': signed_jwt
        }
    )

    if response.status_code != 200:
        raise Exception(f"Failed to get token: {response.text}")

    return response.json()['access_token']

def get_sheet_data(access_token, spreadsheet_id, range_name):
    """Fetch data from Google Sheets API."""
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}"
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to get sheet data: {response.text}")

    return response.json().get('values', [])

def get_spreadsheet_info(access_token, spreadsheet_id):
    """Get spreadsheet metadata including sheet names."""
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}"
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to get spreadsheet info: {response.text}")

    return response.json()

# Main
print("Getting access token...")
token = get_access_token()

print("Fetching spreadsheet info...")
info = get_spreadsheet_info(token, SPREADSHEET_ID)

print(f"\nSpreadsheet: {info['properties']['title']}")
print(f"\nAvailable tabs ({len(info['sheets'])}):")
for sheet in info['sheets']:
    print(f"  - {sheet['properties']['title']}")

# Get data from EMEA CQ Deal Updates
print("\n" + "="*60)
print(f"Exploring '{SHEET_NAME}' tab:")
print("="*60)

try:
    # URL encode the sheet name for spaces
    import urllib.parse
    encoded_range = urllib.parse.quote(f"'{SHEET_NAME}'")
    data = get_sheet_data(token, SPREADSHEET_ID, encoded_range)

    if data:
        headers = data[0]
        print(f"\nColumns ({len(headers)}):")
        for i, h in enumerate(headers):
            print(f"  {i}: {h}")

        print(f"\nTotal rows: {len(data) - 1} (excluding header)")

        print("\nFirst 3 data rows (first 6 columns):")
        for row in data[1:4]:
            display_row = row[:6] if len(row) >= 6 else row
            print(f"  {display_row}")
    else:
        print("No data found")

except Exception as e:
    print(f"Error: {e}")
