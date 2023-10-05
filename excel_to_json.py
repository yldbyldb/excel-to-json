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
    record['keyword'] = record.pop('Keyword')
    record['slug'] = record.pop('URL')
    # replace 'https://societyone.com.au/' string from slug column
    record['slug'] = record['slug'].replace('https://societyone.com.au/', '')
    record['h1'] = record.pop('Heading 1')
    record['title'] = record.pop('Title Tag')
    record['desc'] = record.pop('Meta Desc')
    # remove the 'Len' column
    record.pop('Len')

# Convert back to JSON
json_records = json.dumps(parsed)

# Write to file
with open('ProgrammaticContent.json', 'w') as f:
    f.write(json_records)

# Print finished message
print('Finished writing to JSON file')