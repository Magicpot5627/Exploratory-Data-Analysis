import pandas as pd

# 1. Loading the Dataset
print("--- LOADING DATA ---")
df = pd.read_csv('airline_passenger_satisfaction.csv')


# 2. Checking for Missing Values
print("\n--- CHECKING FOR MISSING VALUES ---")
print("\nisnull() output (first 3 rows):") # Check if values are NaN
print(df.isnull().head(3))
print("\nnotnull() output (first 3 rows):") # Check if values are NOT NaN
print(df.notnull().head(3))
print("\nNumber of NaN values per column:") # Count the number of NaN values in each column
print(df.isnull().sum())

# Total number of missing values in the dataset
print("\nTotal missing values in entire DataFrame:", df.isnull().sum().sum())

# Number of non-NaN values per column
print("\nReported values per column:")
print(df.count())


# 3. Dropping Missing Values
print("\n--- DROPPING MISSING VALUES ---")
print("\nShape after dropna():", df.dropna().shape) # Drop any row that contains at least one NaN value
print("Shape after dropping rows that are entirely NaN:", df.dropna(how='all').shape)
df_dropped_cols = df.dropna(how='all', axis=1)
print("Shape after dropping columns that are entirely NaN:", df_dropped_cols.shape)
print("Shape after dropping columns missing a threshold:", df.dropna(thresh=10, axis=1).shape)


# 4. Mathematical Operations with NaN
print("\n--- MATH OPERATIONS ON COLUMNS WITH NaN ---")
print("Sum of Arrival Delay:", df['Arrival Delay'].sum())
print("Average (Mean) Arrival Delay:", df['Arrival Delay'].mean())
print("\nCumulative Summing of Arrival Delay (first 5 rows):")
print(df['Arrival Delay'].cumsum().head())

# 5. Filling Missing Values
print("\n--- FILLING MISSING VALUES ---")
filledDf = df.fillna(0) # Replace all NaN values in the dataset with 0
print("\nMean of Arrival Delay (Original - NaNs ignored):", df['Arrival Delay'].mean())
print("Mean of Arrival Delay (Filled with 0s):", filledDf['Arrival Delay'].mean())
print("\nForward-filling Arrival Delay (first 5 rows):")
print(df['Arrival Delay'].ffill().head())
print("\nBackward-filling Arrival Delay (first 5 rows):")
print(df['Arrival Delay'].bfill().head())