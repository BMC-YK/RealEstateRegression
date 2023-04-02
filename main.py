import pandas as pd

#Change file PATH
df = pd.read_csv(r"C:\Users\bryan\OneDrive\Desktop\LAB SAVES\RealEstateData.csv")

# Converts TD per Ping to USD per Sq. Ft.
df['Y house price of unit area'] = df['Y house price of unit area'].apply(lambda x: x * 10000 * 0.033 / 35.57).round(decimals = 2)

# Dropping uneccessary columns
df.drop(["No", "X1 transaction date"], inplace=True, axis=1)

# Simplifies column names
df.rename(columns = {'X3 distance to the nearest MRT station':'TS Distance',
                     'X2 house age': 'Age',
                     'X5 latitude': 'Lat',
                     'X6 longitude': 'Long',
                     'Y house price of unit area': 'USD Price',
                     'X4 number of convenience stores': 'CS Distance'}, inplace = True)
