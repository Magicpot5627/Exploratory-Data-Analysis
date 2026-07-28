import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, SimpleImputer

# 1. Loading the Dataset
print("--- LOADING DATA ---")
df = pd.read_csv("airline_passenger_satisfaction.csv")

# Display initial dataset shape and check for missing values per column
print("\nDataset Shape:", df.shape)
print("\nNumber of missing values per column:")
print(df.isnull().sum())


# 2. Mean Imputation (Numerical)
print("\n--- 1. MEAN IMPUTATION (NUMERICAL) ---")
mean_imputer = SimpleImputer(strategy="mean")  # Initialize SimpleImputer with mean strategy
df["Arrival_Delay_Mean"] = mean_imputer.fit_transform(df[["Arrival Delay"]]).ravel()  # Replace missing values with column mean
print("\nArrival Delay filled with Mean (first 5 rows):")  # Display mean imputed values
print(df[["Arrival Delay", "Arrival_Delay_Mean"]].head())


# 3. Median Imputation (Numerical - Robust to Outliers)
print("\n--- 2. MEDIAN IMPUTATION (NUMERICAL) ---")
median_imputer = SimpleImputer(strategy="median"
)  # Initialize SimpleImputer with median strategy
df["Arrival_Delay_Median"] = median_imputer.fit_transform(df[["Arrival Delay"]]).ravel()  # Replace missing values with column median
print("\nArrival Delay filled with Median (first 5 rows):")  # Display median imputed values
print(df[["Arrival Delay", "Arrival_Delay_Median"]].head())


# 4. Mode Imputation (Categorical / Discrete - Most Frequent)
print("\n--- 3. MODE IMPUTATION (CATEGORICAL) ---")
mode_imputer = SimpleImputer(strategy="most_frequent")  # Initialize SimpleImputer with most_frequent strategy
df["Class_Mode"] = mode_imputer.fit_transform(df[["Class"]]).ravel()  # Replace missing values with most frequent value
print("\nClass column filled with Mode (first 5 rows):")  # Display mode imputed values
print(df[["Class", "Class_Mode"]].head())


# 5. MICE Imputation (Multivariate Imputation by Chained Equations)
print("\n--- 4. MICE IMPUTATION (MULTIVARIATE) ---")
num_cols = [
    "Age",
    "Flight Distance",
    "Departure Delay",
    "Arrival Delay",
]  # Select numerical columns required for MICE[cite: 1]
mice_imputer = IterativeImputer(max_iter=10, random_state=42)  # Initialize IterativeImputer with fixed random state[cite: 1]

# Perform MICE imputation on selected numerical columns
df_mice_imputed = pd.DataFrame(
    mice_imputer.fit_transform(df[num_cols]),
    columns=[f"{col}_MICE" for col in num_cols],
)
df["Arrival_Delay_MICE"] = df_mice_imputed["Arrival Delay_MICE"]  # Add imputed MICE values back to main DataFrame


# 6. Comparing Results Across Imputation Methods
print("\n--- IMPUTATION RESULTS COMPARISON ---")
missing_rows = df[df["Arrival Delay"].isnull()]  # Filter original missing rows to verify output
comparison = missing_rows[
    [
        "ID",
        "Departure Delay",
        "Arrival Delay",
        "Arrival_Delay_Mean",
        "Arrival_Delay_Median",
        "Arrival_Delay_MICE",
    ]
]
print("\nComparison of Imputation Methods on Missing 'Arrival Delay' Rows:")
print(comparison.to_string(index=False))