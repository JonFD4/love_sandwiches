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

    #Accessing spreadsheet and checking

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS= CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


''' Getting sales data from our user. Request for users to enter their data into terminal
This will be saved as CSV- comma separated values- allows data to be saved in a table format. '''

def get_sales_data():
    '''Get sales figures input from the user'''
    print("Please enter sales data from the last market")
    print("Data should be six numbers, separated by commas")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    print(f" The data provided is {data_str}")


get_sales_data()