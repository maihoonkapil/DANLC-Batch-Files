import pandas as pd
import numpy as np

df = pd.DataFrame({'ord_no': [np.nan, np.nan, 70002.0, np.nan, np.nan, 70005.0, np.nan, 70010.0, 70003.0, 70012.0, np.nan, np.nan],
                   'purch_amt': [np.nan, 270.65, 65.26, np.nan, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, np.nan],
                   'ord_date': ['2012-09-10', np.nan, np.nan, '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', np.nan],
                   'customer_id': [np.nan, 3001.0, 3001.0, np.nan, 3002.0, 3001.0, 3004.0, 3003.0, 3002.0, 3001.0, np.nan, np.nan]})

print("Original Orders DataFrame:")
print(df)

print("\nDrop those rows in which specific columns have missing values:")
df1 = df.dropna(subset=['ord_no', 'purch_amt', 'ord_date', 'customer_id'])
print(df1)