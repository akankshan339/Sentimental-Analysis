import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load the dataset
input_file = 'total.csv'  # Replace with your input CSV file name
output_file = 'preprocessed_comments.csv'  # Replace with your desired output CSV file name

df = pd.read_csv(input_file)

# Initialize Porter Stemmer and stopwords
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Tokenize the text
    words = word_tokenize(text)
    
    # Remove punctuation and convert to lowercase
    words = [word.lower() for word in words if word.isalpha()]
    
    # Remove stopwords and perform stemming
    words = [ps.stem(word) for word in words if word not in stop_words]
    
    # Reconstruct the text
    text = ' '.join(words)
    
    return text

# Apply preprocessing to the 'Comment' column
df['Processed Comment'] = df['Comment'].apply(preprocess_text)

# Save the preprocessed comments to a new CSV file
df.to_csv(output_file, index=False)

print(f"Preprocessed comments have been written to {output_file}")
