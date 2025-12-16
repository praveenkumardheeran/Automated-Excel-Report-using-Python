import pandas as pd


# Step 1: Read the raw CSV file
df = pd.read_csv("raw_data.csv")

# Step 2: Remove completely empty rows
df = df.dropna()

# Step 3: Save cleaned data to Excel file
df.to_excel("clean_report.xlsx", index=False)

print("Excel report created successfully")
