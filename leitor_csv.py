import os
import pandas as pd
import json
import html
import re

def remove_html_tags(text):
    text = html.unescape(text)
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

current_dir = os.path.dirname(__file__)
csv_file_python = os.path.join(current_dir, 'QueryResults_python_442.csv')

df = pd.read_csv(csv_file_python)

for index, row in df.iterrows():
    if 'Title' in row and pd.notnull(row['Title']) and 'python' in row['Title'].lower():
        row['Body'] = remove_html_tags(row['Body'])
        row['AcceptedAnswer'] = remove_html_tags(row['AcceptedAnswer'])
        with open('python_questions.json', 'a') as f:
            f.write(json.dumps(row.to_dict(), indent=4) + '\n')
            
            
csv_file_java = os.path.join(current_dir, 'QueryResults_java_182.csv')

df = pd.read_csv(csv_file_java)

for index, row in df.iterrows():
    if 'Title' in row and pd.notnull(row['Title']) and 'java' in row['Title'].lower():
        row['Body'] = remove_html_tags(row['Body'])
        row['AcceptedAnswer'] = remove_html_tags(row['AcceptedAnswer'])
        with open('java_questions.json', 'a') as f:
            f.write(json.dumps(row.to_dict(), indent=4) + '\n')