import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Read the cleaned comments CSV file
df = pd.read_csv('CleanedAiComment.csv')

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to get sentiment label
def get_sentiment(comment):
    # if comments in dataset contains missing values either we return neturel or remove those NaN values during data preprocessing 
    if pd.isna(comment):
        return 'neutral'
    
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
df[['Comment', 'Sentiment']].to_csv('LabeledAiComment.csv', index=False)

print("Labeling complete! Check the 'LabeledAiComment.csv' file.")




# import pandas as pd
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# # Load the cleaned comments CSV file
# df = pd.read_csv('Cleaned_Comments.csv')

# # Initialize VADER sentiment analyzer
# analyzer = SentimentIntensityAnalyzer()

# # Function to get sentiment label
# def get_sentiment(comment):
#     score = analyzer.polarity_scores(comment)['compound']
#     if score >= 0.05:
#         return 'positive'
#     elif score <= -0.05:
#         return 'negative'
#     else:
#         return 'neutral'

# # Apply the sentiment function to all comments
# df['Sentiment'] = df['Cleaned_Comments'].apply(get_sentiment)

# # Save the labeled comments to a new CSV file
# df.to_csv('LabeledAiComment.csv', index=False)

# print("Labeling complete! Check the 'Labeled_Comments.csv' file.")
