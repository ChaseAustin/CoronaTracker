"""
Coronavirus Tracker Upload to Google Sheets

Chase Austin (chase7867@gmail.com)
"""

import COVID19Py
from datetime import date
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import time

# get google sheet
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
gc = gspread.authorize(credentials)
worksheet = gc.open("Coronavirus Tracker Data").sheet1

# get json data
covid19 = COVID19Py.COVID19(data_source="csbs")
data = covid19.getLocationByCountryCode("US")

# get date
#today = date.today().strftime("%d/%m/%Y")

# add header
worksheet.update("A1", [["Date", "LastUpdated", "Country", "State", "County", "Latitude", "Longitude", "Confirmed", "Deaths", "Recovered"]])
nextRow = len(worksheet.get_all_values()) + 1


# loop through json data
for row in data:

    print(str(nextRow-1))
    # cell info
    date = "03/24/2020"
    lastUpdated = row["last_updated"]
    country = "US"
    state = row["province"]
    county = row["county"]
    latitude = row["coordinates"]["latitude"]
    longitude = row["coordinates"]["longitude"]
    confirmed = row["latest"]["confirmed"]
    deaths = row["latest"]["deaths"]
    recovered = row["latest"]["recovered"]

    # upload to google sheets
    worksheet.update("A" + str(nextRow), [[date, lastUpdated, country, state, county, latitude, longitude, confirmed, deaths, recovered]])
    
    # Google Sheets API has a limit of 500 requests per 100 seconds per project, and 100 requests per 100 seconds per user
    time.sleep(1)

    # increment next row
    nextRow = nextRow + 1