import csv
import nltk
from nltk.tokenize import word_tokenize
import os

# Download the NLTK tokenizer data (only needs to be done once)
nltk.download('punkt')

def tokenize_comments(input_file, output_file):
    # Read the CSV file
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Process each row
    tokenized_rows = []
    for row in rows:
        tokenized_row = []
        for item in row:
            # Tokenize the comment
            tokens = word_tokenize(item)
            tokenized_row.extend(tokens)  # Use extend to flatten the list
        tokenized_rows.append(tokenized_row)
    
    # Write the tokenized comments to a new CSV file
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(tokenized_rows)
    except PermissionError:
        print(f"Permission denied: Unable to write to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with an absolute path
input_path = os.path.abspath('noPunctAicomment.csv')
output_path = os.path.abspath('tokenizedAicomment.csv')

tokenize_comments(input_path, output_path)



'''import csv
import nltk
from nltk.tokenize import word_tokenize

# Download the NLTK tokenizer data (only needs to be done once)
nltk.download('punkt')

def tokenize_comments(input_file, output_file):
    # Read the CSV file
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Process each row
    tokenized_rows = []
    for row in rows:
        tokenized_row = []
        for item in row:
            # Tokenize the comment
            tokens = word_tokenize(item)
            tokenized_row.append(tokens)
        tokenized_rows.append(tokenized_row)
    
    # Write the tokenized comments to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in tokenized_rows:
            # Join the tokens with spaces for saving in CSV
            writer.writerow([' '.join(tokens) for tokens in row])

# Example usage
tokenize_comments('noPunctAicomment.csv', 'tokenizedAicomment.csv')
'''
