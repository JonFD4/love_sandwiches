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

    # Accessing spreadsheet and checking

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
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
    sales_data = data_str.split(",")
    validate_data(sales_data)


""" Ths validates the data given by user. If the data is wrong, it might break the program.
With this function, the program will output a message to the user informing them about what is wrong.

Inside the function is the try statement. Inside it, the program will convert all string values into integers.
Raises ValueError if strings cannot be converted into int or if there aren't exactly 6 values.
"""


def validate_data(values):
  
  try:
    [int(value) for value in values]
    if len(values) != 6:
        raise ValueError(f"Exactly 6 values required, you provided {len(values)}")
     
  except ValueError as e:
    print(f"Invalid data: {e}, please try again. \n")
get_sales_data()