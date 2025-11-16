import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from flask import Flask, request, render_template
import joblib

# Download necessary NLTK data files
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

app = Flask(__name__)

# Load the trained model and the TF-IDF vectorizer
model = joblib.load('sentiment_model.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')


# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_comment(comment):
    # Lowercase
    comment = comment.lower()

    # Remove emojis
    comment = re.sub(r'[^\x00-\x7F]+', '', comment)
    
    # Remove punctuation and numbers
    comment = re.sub(r'[^\w\s]', '', comment)
    comment = re.sub(r'\d+', '', comment)
    
    # Remove single characters
    comment = re.sub(r'\b\w\b', '', comment)

    # Normalize whitespace
    comment = re.sub(r'\s+', ' ', comment).strip()
    
    # Remove URLs
    comment = re.sub(r'http\S+|www\S+|https\S+', '', comment, flags=re.MULTILINE)
    
    # Tokenize comment
    tokens = nltk.word_tokenize(comment)
    
    # Remove stopwords
    tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # Join tokens back to string
    cleaned_comment = ' '.join(tokens)
    
    return cleaned_comment

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        print("POST request received")
        comment = request.form['comment']
        cleaned_comment = preprocess_comment(comment)
        comment_tfidf = tfidf_vectorizer.transform([cleaned_comment])
        prediction = model.predict(comment_tfidf)
        return render_template('result.html', prediction=prediction[0])


if __name__ == "__main__":
    app.run(debug=True)
