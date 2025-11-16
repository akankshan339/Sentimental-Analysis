import pandas as pd
from googletrans import Translator
import csv

def translate_hindi_comments(csv_file, output_file):
    translator = Translator()
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    translated_rows = []
    for row in rows:
        translated_row = []
        for comment in row:
            try:
                if comment and comment.strip():  # Check if comment is not None and not empty
                    translated_comment = translator.translate(comment, src='hi', dest='en').text
                    translated_row.append(translated_comment)
                else:
                    translated_row.append("")  # Append empty string for empty comments or NoneType comments
            except Exception as e:
                print(f"Error translating comment: {comment}, Error: {e}")
                translated_row.append("")  # Append empty string if translation fails
        translated_rows.append(translated_row)
    
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(translated_rows)

# Example usage:
translate_hindi_comments(r'total.csv', 'converted.csv')
#translate_hindi_comments(r'C:\Users\hp\Downloads\total.csv', 'converted.csv')



'''import pandas as pd
from google.cloud import translate_v2 as translate

# Load the dataset
input_file = 'total.csv'  # Replace with your input CSV file name
output_file = 'translated_comments.csv'  # Replace with your desired output CSV file name

# Initialize the Translation client
translate_client = translate.Client()

def translate_to_english(text):
    # Translate the text from Hindi to English
    translation = translate_client.translate(text, target_language='en')
    return translation['translatedText']

# Read the CSV file with Hindi comments
df = pd.read_csv(input_file)

# Translate Hindi comments to English
df['Translated Comment'] = df['Comment'].apply(translate_to_english)

# Save the translated comments to a new CSV file
df.to_csv(output_file, index=False)

print(f"Translated comments have been written to {output_file}")'''

