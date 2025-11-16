punctuations = '''()-[]{};:'"\,<>./?@#$%^&*_~'''

import csv
import string

def remove_punctuation_from_comments(input_file, output_file):
    # Define punctuations to remove
    punctuations = string.punctuation
    
    # Read the CSV file
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Process each row
    updated_rows = []
    for row in rows:
        updated_row = []
        for item in row:
            # Remove punctuations
            no_punct = ''.join(ch for ch in item if ch not in punctuations)
            updated_row.append(no_punct)
        updated_rows.append(updated_row)
    
    # Write to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

# Example usage
remove_punctuation_from_comments('emojiRemoveAicomment.csv', 'noPunctAicomment.csv')


