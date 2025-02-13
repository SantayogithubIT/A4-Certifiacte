import pandas as pd

# Read the Excel file
df = pd.read_csv('PR CERTI.csv')
list_names = df.values.tolist()
# Display the list
print(list_names)
