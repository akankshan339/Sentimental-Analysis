import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Download necessary NLTK data files
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

# Read the extracted comments CSV file
df = pd.read_csv('ExtractAiComment.csv')

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Function to clean comments
def preprocess_comment(comment):
    # Remove emojis
    comment = re.sub(r'[^\x00-\x7F]+', '', comment)
    
    # Remove punctuation and numbers
    comment = re.sub(r'[^\w\s]', '', comment)
    comment = re.sub(r'\d+', '', comment)
    
    # Remove single characters
    comment = re.sub(r'\b\w\b', '', comment)
    
    # Tokenize comment
    tokens = nltk.word_tokenize(comment)
    
    # Remove stopwords
    tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Remove duplicate words
    tokens = list(dict.fromkeys(tokens))
    
    # Lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # Join tokens back to string
    cleaned_comment = ' '.join(tokens)
    
    return cleaned_comment

# Apply the preprocessing function to all comments
df['Comment'] = df['Comment'].apply(preprocess_comment)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to get sentiment label
def get_sentiment(comment):
    score = analyzer.polarity_scores(comment)['compound']
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Apply the sentiment function to all comments
df['Sentiment'] = df['Comment'].apply(get_sentiment)

# Save the comments and sentiment labels to a new CSV file with only 'Comment' and 'Sentiment' columns
df[['Comment', 'Sentiment']].to_csv('Labeled_Comments.csv', index=False)

print("Labeling complete! Check the 'Labeled_Comments.csv' file.")
