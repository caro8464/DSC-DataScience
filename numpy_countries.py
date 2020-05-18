import pandas as ps
import numpy as np

countries = ps.read_csv('countries.csv')
df = ps.DataFrame(countries)

print(df)                                                         # All
print(df.columns)                                                 # Columns
print(df.index)                                                   # Rows
print(df.size)                                                    # Size
print(df.head)                                                    # Head
print(df.shape)                                                   # Shape
print(df.axes)                                                    # Axes
print(df.iloc[-4:])                                               # Last 4 Rows
print(df.loc[df.Currency == 'EUR'])                               # All countries with Euro
print(df[['Name','Currency']])                                    # Display only Name and Currency
print(df.loc[df.BIP > 2000])                                      # BIP greater than 2000
print(df[(df.People > 50000000) & (df.People < 150000000)])       # Habitants between 50 MIO and 150 MIO
print(df.rename(columns={'BIP':'Bip'}))                           # Rename BIP with Bip
print(df.sum().BIP)                                               # Sum of BIP
print(df.sort_values(by='Name'))                                  # Sort by Name alphabetically
print(df.median().People)                                         # Median of People

# New DataFrame and changing values conditional
df2 = df
df2.Area = np.where(df2.Area > 1000000, 'BIG', 'SMALL')
print(df2)