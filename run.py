import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
'''IAM stands for Identity and Access Management. 
    It is a configuration present in all google accounts. It specifies what the user has access to. 
    The scope lists the APIs that the prohram should access in order to run. Our scope value will not change, therefore it is known as a constant variable, therefore written in capitals
    '''

    #Accessing spreadsheet 

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS= CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')
sales = SHEET.worksheet('sales') # corresponds to the name of the worksheet given in google spreadsheet

data = sales.get_all_values()
print(data)