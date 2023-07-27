import os
import locale
from dotenv import load_dotenv

import pandas as pd
from twilio.rest import Client

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

'''
Briefing
- open .csv files
- for each file:
    - check if any value in the "sales" column  is greater than 5500
    - if it is greater than 55,000 then send SMS with the seller's name, month and price
    
dependecies
- pandas
- openpyxl
- twillio
'''

# read environment variables
load_dotenv()

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
TWILLIO_NUMBER = os.getenv('TWILLIO_NUMBER')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

mouths_list = ['janeiro', 'fevereiro',  'marco']

for mouth in mouths_list:
    sales_table = pd.read_csv(f'./sales/{mouth}.csv')

    has_bonus = sales_table['sales'] > 55000

    if has_bonus.any():
        seller = sales_table.loc[has_bonus, 'seller'].values[0]
        sales = locale.currency(sales_table.loc[has_bonus, 'sales'].values[0])

        if mouth == 'marco':
            mouth = 'março'

        message = client.messages.create(
            from_=TWILLIO_NUMBER,
            to=PHONE_NUMBER,
            body=f'No mês {mouth.capitalize()} o/a vendedor(a) {seller} , vendeu {sales} e ganhou o bonus!'
        )
        print(message.sid)


