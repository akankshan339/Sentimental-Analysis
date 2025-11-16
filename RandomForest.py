import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer

#load the dataset
data= pd.read_csv('LabeledAiComment.csv')

data.dropna(subset=['Comment'], inplace =True)

# Split the data into features (Comments) and target variables (label)
x = data['Comment']  # features
y = data['Sentiment'] # target variables

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(max_features=2000)
X = tfidf_vectorizer.fit_transform(x)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=82)

rf_classifier=RandomForestClassifier(n_estimators=100, random_state=82)

# Train the Random Forest model
rf_classifier.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Classification Report:")
# print(classification_report(y_test, y_pred))