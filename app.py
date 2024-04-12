import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

max_price = ds["price"].max()

print("El precio más alto es:", max_price)

