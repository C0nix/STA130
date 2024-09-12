import pandas as pd

# URL of the dataset
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"

# Read the CSV from the URL using 'latin1' encoding
df = pd.read_csv(url, encoding='latin1')

# Display the entire DataFrame
display(df)


import pandas as pd

# URL of the dataset
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"

# Read the CSV from the URL using 'latin1' encoding
df = pd.read_csv(url, encoding='latin1')

# Display the entire DataFrame
display(df)

# Print the number of rows and columns without changing the display format
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")


import pandas as pd

# URL of the dataset
url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"

# Read the CSV from the URL using 'latin1' encoding
df = pd.read_csv(url, encoding='latin1')

# Display the entire DataFrame
display(df)

# Get missing values count using .isna()
missing_values = df.isna().sum()

# Filter out columns with missing values
missing_summary = missing_values[missing_values > 0]

# Separate numerical and categorical columns with missing values
numerical_missing = [col for col in missing_summary.index if pd.api.types.is_numeric_dtype(df[col])]
categorical_missing = [col for col in missing_summary.index if pd.api.types.is_object_dtype(df[col])]

# Print the summary of missing data for numerical columns
print("Missing Data Summary for Numerical Columns:")
for column in numerical_missing:
    print(f"{column}: {missing_summary[column]} missing")

# Print the summary of missing data for categorical columns
print("\nMissing Data Summary for Categorical Columns:")
for column in categorical_missing:
    print(f"{column}: {missing_summary[column]} missing")


df.isna().sum()

import pandas as pd

# URL of the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

# Read the CSV from the URL using 'latin1' encoding
df = pd.read_csv(url, encoding='latin1')

# Display the entire DataFrame
display(df)

# Get missing values count using .isna()
missing_values = df.isna().sum()

# Filter out columns with missing values
missing_summary = missing_values[missing_values > 0]

# Separate numerical and categorical columns with missing values
numerical_missing = [col for col in missing_summary.index if pd.api.types.is_numeric_dtype(df[col])]
categorical_missing = [col for col in missing_summary.index if pd.api.types.is_object_dtype(df[col])]

# Print the summary of missing data for numerical columns
print("Missing Data Summary for Numerical Columns:")
for column in numerical_missing:
    print(f"{column}: {missing_summary[column]} missing")

# Print the summary of missing data for categorical columns
print("\nMissing Data Summary for Categorical Columns:")
for column in categorical_missing:
    print(f"{column}: {missing_summary[column]} missing")


import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Group by 'sex' and describe the 'age' column for each group
grouped_summary = df.groupby('sex')['age'].describe()

# Display the result explicitly
grouped_summary


import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Drop rows where the 'age' column has missing (NaN) values
df_cleaned = df.dropna(subset=['age'])

# Group by 'sex' and describe the 'age' column for each group after cleaning missing data
grouped_summary = df_cleaned.groupby('sex')['age'].describe()

# Display the result
grouped_summary


import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Group by 'sex' and describe the 'age' column for each group
grouped_summary = df.groupby('alive')['age'].describe()

# Display the result explicitly
grouped_summary


#A

url = "https://raw.githubusercontent.com/pointOfive/STA130_F23/main/Data/amazonbooks.csv"
print(url)

df = pd.read_csv(url, encoding='latin1') #latin1 = ISO-8859-1
print(df.shape) #To print out in the format of a table 
df

#B

import pandas as py

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanics.csv"
print(url)

df = pd.read_csv(url, encoding='latin1') #latin1 = ISO-8859-1
print(df.shape) #To print out in the format of a table 
df

#C

import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Group by 'sex' and describe the 'age' column for each group
grouped_summary = Df.groupby('alive')['age'].describe()

# Display the result explicitly
grouped_summary

#D

import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url

# Group by 'sex' and describe the 'age' column for each group
grouped_summary = df.groupby('alive')['age'].describe()

# Display the result explicitly
grouped_summary

#E

import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Group by 'sex' and describe the 'age' column for each group
grouped_summary = df.groupby('Sex')['age'].describe()

# Display the result explicitly
grouped_summary

#F

import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Group by 'sex' and describe the 'age' column for each group
grouped_summary = df.groupby('sex')['Age'].describe()

# Display the result explicitly
grouped_summary

#G

import pandas as pd

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

# Group by 'sex' and describe the 'age' column for each group
grouped_summary = titanic_df.groupby('sex')['age'].describe()

# Display the result explicitly
grouped_summary
