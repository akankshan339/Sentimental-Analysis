import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer


labeled_comments_df = pd.read_csv('LabeledAiComment.csv')
labeled_comments_df.head()


features_df = pd.read_csv('TFIDF_Features.csv')

# Fill NaN values in 'Comment' column with an empty string and ensure all entries are strings
labeled_comments_df['Comment'] = labeled_comments_df['Comment'].fillna('').astype(str)

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(max_features=2000)
X = tfidf_vectorizer.fit_transform(labeled_comments_df['Comment']).toarray()


# Extract the labels (sentiment)
labels = labeled_comments_df['Sentiment']

# Print the shape of the feature matrix and labels
print("Shape of the feature matrix (X):", X.shape)
print("Shape of the labels (y):", labels.shape)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train the logistic regression model
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))

# print("Classification Report:")
# print(classification_report(y_test, y_pred))










# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import classification_report, accuracy_score
# from sklearn.feature_extraction.text import TfidfVectorizer
# import joblib
# import re
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')

# # Load the labeled comments CSV file
# labeled_comments_df = pd.read_csv('LabeledAiComment.csv')

# # Preprocess comments
# stop_words = set(stopwords.words('english'))
# lemmatizer = WordNetLemmatizer()

# def preprocess_comment(comment):
#     if pd.isna(comment):
#         return ''
#     # Lowercase
#     comment = comment.lower()  
#     # Remove emojis
#     comment = re.sub(r'[^\x00-\x7F]+', '', comment)
#     # Remove punctuation and numbers
#     comment = re.sub(r'[^\w\s]', '', comment)
#     comment = re.sub(r'\d+', '', comment)
#     # Remove single characters
#     comment = re.sub(r'\b\w\b', '', comment)
#     # Normalize whitespace
#     comment = re.sub(r'\s+', ' ', comment).strip()  
#     # Remove URLs
#     comment = re.sub(r'http\S+|www\S+|https\S+', '', comment, flags=re.MULTILINE)  
#     # Tokenize comment
#     tokens = nltk.word_tokenize(comment)
#     # Remove stopwords
#     tokens = [word for word in tokens if word.lower() not in stop_words]
#     # Remove duplicate words
#     tokens = list(dict.fromkeys(tokens))
#     # Lemmatization
#     tokens = [lemmatizer.lemmatize(word) for word in tokens]
#     # Join tokens back to string
#     cleaned_comment = ' '.join(tokens)
#     return cleaned_comment

# labeled_comments_df['Comment'] = labeled_comments_df['Comment'].apply(preprocess_comment)

# # TF-IDF Vectorization
# tfidf_vectorizer = TfidfVectorizer(max_features=5000)
# X = tfidf_vectorizer.fit_transform(labeled_comments_df['Comment']).toarray()

# # Save the TF-IDF vectorizer
# joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')

# # Extract the labels (sentiment)
# labels = labeled_comments_df['Sentiment']

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# # Train the logistic regression model
# model = LogisticRegression(max_iter=1000)
# model.fit(X_train, y_train)

# # Make predictions on the testing set
# y_pred = model.predict(X_test)

# # Evaluate the model
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Classification Report:")
# print(classification_report(y_test, y_pred))

# # Save the trained model to a file
# joblib.dump(model, 'sentiment_model.pkl')

# print("Model training and saving complete!")



