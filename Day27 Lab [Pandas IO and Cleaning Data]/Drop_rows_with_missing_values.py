import pandas as pd
import numpy as np

df = pd.DataFrame({
    'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10',
                 '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
    'salesman_id': [5002, 5003, 5001, np.nan, 5002, 5001, 5001, np.nan, 5003, 5002, 5003, np.nan]
})

df.dropna(inplace=True)

print("DataFrame after dropping missing values:")
print(df)

total_purchase = df['purch_amt'].sum()
print("\nTotal Purchase Amount:", total_purchase)

customer_totals = df.groupby('customer_id')['purch_amt'].sum().reset_index()
print("\nTotal Purchase Amount per Customer:")
print(customer_totals)

df['ord_date'] = pd.to_datetime(df['ord_date'])

df['year'] = df['ord_date'].dt.year
print("\nDataFrame with Year Extracted:")
print(df)