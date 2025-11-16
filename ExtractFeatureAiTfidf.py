import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Read the extracted comments CSV file
df = pd.read_csv('CleanedAiComment.csv')

# Fill NaN values in 'Comment' column with empty string using a direct assignment
df['Comment'] = df['Comment'].fillna('')

# Initialize TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=1000)  # Adjust max_features as needed

# Fit-transform the 'Comment' column
tfidf_features = tfidf_vectorizer.fit_transform(df['Comment'])

# Convert to DataFrame for easier handling (optional)
tfidf_df = pd.DataFrame(tfidf_features.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

# Save the TF-IDF features to a new CSV file (optional)
tfidf_df.to_csv('TFIDF_Features.csv', index=False)

print("TF-IDF feature extraction complete! Check the 'TFIDF_Features.csv' file.")
