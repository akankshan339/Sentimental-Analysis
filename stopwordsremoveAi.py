import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os

# Download the NLTK tokenizer and stopwords data (only needs to be done once)
nltk.download('punkt')
nltk.download('stopwords')

def tokenize_and_remove_stopwords(input_file, output_file):
    # Define the list of stopwords
    stop_words = set(stopwords.words('english'))

    # Read the CSV file
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Process each row
    cleaned_rows = []
    for row in rows:
        cleaned_row = []
        for item in row:
            # Tokenize the comment
            tokens = word_tokenize(item)
            # Remove stopwords
            filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
            cleaned_row.extend(filtered_tokens)  # Use extend to flatten the list
        cleaned_rows.append(cleaned_row)
    
    # Write the cleaned comments to a new CSV file
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(cleaned_rows)
    except PermissionError:
        print(f"Permission denied: Unable to write to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with an absolute path
input_path = os.path.abspath('tokenizedAicomment.csv')
output_path = os.path.abspath('stopwordRemoveAicomment.csv')

tokenize_and_remove_stopwords(input_path, output_path)