import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string
import os

# Download the necessary NLTK data (only needs to be done once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

# Function to map POS tag to first character lemmatize() accepts
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def process_comments(input_file, output_file):
    # Define the list of stopwords
    stop_words = set(stopwords.words('english'))
    # Define punctuations to remove
    punctuations = string.punctuation
    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Read the CSV file
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Process each row
    processed_rows = []
    for row in rows:
        processed_row = []
        for item in row:
            # Remove punctuation
            no_punct = ''.join(ch for ch in item if ch not in punctuations)
            # Tokenize the comment
            tokens = word_tokenize(no_punct)
            # Remove stopwords
            filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
            # Get POS tags for better lemmatization
            pos_tags = nltk.pos_tag(filtered_tokens)
            # Lemmatize each token
            lemmatized_tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(pos)) for token, pos in pos_tags]
            # Add lemmatized tokens to the row
            processed_row.extend(lemmatized_tokens)  # Use extend to flatten the list
        processed_rows.append(processed_row)
    
    # Write the processed comments to a new CSV file
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(processed_rows)
    except PermissionError:
        print(f"Permission denied: Unable to write to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with an absolute path
input_path = os.path.abspath('emojiRemoveAicomment.csv')
output_path = os.path.abspath('PreprocessAicomment.csv')

process_comments(input_path, output_path)