"""
Data Audit Script

This script performs an initial audit of the raw supply chain dataset.

Purpose of this step:
To understand the dataset structure and perform basic data quality checks
before starting the data cleaning and analysis phases.

The audit includes:
1. Dataset preview
2. Dataset shape
3. Column names
4. Data types
5. Missing value analysis
6. Duplicate record detection
7. Statistical summary of numerical columns
8. Unique value analysis for categorical columns
"""

# -------------------------------------------------
# Import Required Libraries
# -------------------------------------------------

import pandas as pd
from pathlib import Path

print("========== SUPPLY CHAIN DATA AUDIT ==========\n")


# -------------------------------------------------
# 1. Locate Project Root (portable)
# -------------------------------------------------

# Identify the current script location
script_path = Path(__file__).resolve()

# Navigate to the project root folder
project_root = script_path.parents[1]

# Define dataset path
data_path = project_root / "02_Data" / "CSV file" / "raw_data.csv"

print("Script Location:", script_path)
print("Project Root:", project_root)
print("Dataset Path:", data_path)
print()


# -------------------------------------------------
# 2. Validate dataset path
# -------------------------------------------------

if not data_path.exists():
    raise FileNotFoundError(f"Dataset not found at: {data_path}")


# -------------------------------------------------
# 3. Load dataset
# -------------------------------------------------

df = pd.read_csv(data_path)


# -------------------------------------------------
# 4. Basic dataset overview
# -------------------------------------------------

print("========== DATASET PREVIEW ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DATA TYPES ==========")
print(df.dtypes)


# -------------------------------------------------
# 5. Data quality checks
# -------------------------------------------------

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())


# -------------------------------------------------
# 6. Numerical statistics
# -------------------------------------------------

print("\n========== BASIC STATISTICS ==========")
print(df.describe())


# -------------------------------------------------
# 7. Categorical column analysis
# -------------------------------------------------

print("\n========== UNIQUE VALUES IN CATEGORICAL COLUMNS ==========")

categorical_cols = df.select_dtypes(include=["object", "string"]).columns

for col in categorical_cols:
    print(f"\nColumn: {col}")
    print("Unique values:", df[col].nunique())
    print(df[col].unique())


print("\n========== DATA AUDIT COMPLETE ==========")