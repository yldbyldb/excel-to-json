import pandas as pd
import json

# Read the excel file
df = pd.read_excel('data.xlsx') # data.xlsx in the same folder

# Convert to JSON
json_records = df.to_json(orient='records')

# Parse the JSON
parsed = json.loads(json_records)

# Change the key names
for record in parsed:
    record['usa'] = record.pop('Monthly Search Vol (USA)')
    record['name'] = record.pop('Suggested Programmatic Keyword')

# Convert back to JSON
json_records = json.dumps(parsed)

# Write to file
with open('data.json', 'w') as f:
    f.write(json_records)

# Print finished message
print('Finished writing to JSON file')