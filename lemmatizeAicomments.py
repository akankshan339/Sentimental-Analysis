import csv
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
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

def lemmatize_comments(input_file, output_file):
    lemmatizer = WordNetLemmatizer()

    # Read the CSV file
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Process each row
    lemmatized_rows = []
    for row in rows:
        lemmatized_row = []
        for item in row:
            tokens = item.split()  # Assuming tokens are space-separated in the cells
            # Get POS tags for better lemmatization
            pos_tags = nltk.pos_tag(tokens)
            # Lemmatize each token
            lemmatized_tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(pos)) for token, pos in pos_tags]
            lemmatized_row.extend(lemmatized_tokens)  # Use extend to flatten the list
        lemmatized_rows.append(lemmatized_row)
    
    # Write the lemmatized comments to a new CSV file
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(lemmatized_rows)
    except PermissionError:
        print(f"Permission denied: Unable to write to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with an absolute path
input_path = os.path.abspath('stopwordRemoveAicomment.csv')
output_path = os.path.abspath('lemmatizedAicomment.csv')

lemmatize_comments(input_path, output_path)


'''import csv
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import os

# Download the NLTK WordNet data (only needs to be done once)
nltk.download('wordnet')
nltk.download('omw-1.4')

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

def lemmatize_comments(input_file, output_file):
    lemmatizer = WordNetLemmatizer()

    # Read the CSV file
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Process each row
    lemmatized_rows = []
    for row in rows:
        lemmatized_row = []
        for item in row:
            tokens = item.split()  # Assuming tokens are space-separated in the cells
            # Get POS tags for better lemmatization
            pos_tags = nltk.pos_tag(tokens)
            # Lemmatize each token
            lemmatized_tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(pos)) for token, pos in pos_tags]
            lemmatized_row.extend(lemmatized_tokens)  # Use extend to flatten the list
        lemmatized_rows.append(lemmatized_row)
    
    # Write the lemmatized comments to a new CSV file
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(lemmatized_rows)
    except PermissionError:
        print(f"Permission denied: Unable to write to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with an absolute path
input_path = os.path.abspath('stopwordRemoveAicomment.csv')
output_path = os.path.abspath('lemmatizedAicomment.csv')

lemmatize_comments(input_path, output_path)

'''