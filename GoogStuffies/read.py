import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
from gspread_dataframe import set_with_dataframe
import pandas as pd
import glob

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)

sheet = client.open("HealthcareMapprSheets").sheet1   

txt_file = glob.glob("/Users/alan/HealthcareMappr/GoogStuffies/test/blah.txt")
print(txt_file)

data = pd.read_csv(txt_file[0], header = 0)
sheet.clear()
set_with_dataframe(worksheet=sheet, dataframe=data, include_index=False,
include_column_header=True, resize=True)
