import pandas as pd

# Read the generated alerts file
df = pd.read_csv("data/alerts.csv")

# Convert CSV data into JSON
df.to_json(
    "data/insider_activity.json",
    orient="records",
    lines=True
)

print("JSON file created successfully.")