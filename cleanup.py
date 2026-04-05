import pandas as pd

df = pd.read_csv('./csv/supermarket_sales_dirty.csv')
df = df.dropna().drop_duplicates()

df.columns = [x.upper() for x in df.columns]

text_cols = ['INVOICE_ID', 'BRANCH', 'CITY', 'CUSTOMER_TYPE', 
             'GENDER_CUSTOMER', 'PRODUCT_LINE', 'PAYMENT_METHOD']

for col in text_cols:
    if col in df.columns:
        df[col] = df[col].str.strip()
        if col in ['CUSTOMER_TYPE', 'GENDER_CUSTOMER', 'CITY', 'PRODUCT_LINE']:
            df[col] = df[col].str.title()   # "Yangon", "Member", "Male", "Sports And Travel"
        elif col == 'PAYMENT_METHOD':
            df[col] = df[col].str.title()   # "Credit Card", "Cash", "Ewallet"
        elif col == 'BRANCH':
            df[col] = df[col].str.upper()   # "A", "B", "C"

df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')
df.to_csv('./csv/supermarket_sales_cleaned.csv', index=False)