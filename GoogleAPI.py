
# %%
import pandas as pd     
#import Library for python   
gsheetid = "10pm-mtarXBLWvX-YMl4iymHfNykmld-KZhh8qNMkT_A"     #gsheetid = "<Goole Sheets>"
#Extract part of the Google Sheet address
sheet_name = "korosh"
#Google Sheet name published
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
# Do not edit
df = pd.read_csv(gsheet_url)
df

 # %%
 from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import pdftables_api
#import Library for python   

g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

#Google Sheet name published

c = pdftables_api.Client('insert_API_key')
c.csv('input_file_name.pdf', 'output_file_name')

with open("output_file_name.csv","r") as file:
	file_drive = drive.CreateFile({'title':os.path.basename(file.name) })  
	file_drive.SetContentString(file.read()) 
	file_drive.Upload()
# %%
