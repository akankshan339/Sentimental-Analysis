import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time

api_key = "AIzaSyBtWgI_szcCWGNW-Ht7X4X9DhzQLam9vbk"  # Replace with your own API key
youtube = build('youtube', 'v3', developerKey=api_key)

# Replace with your own live chat ID
live_chat_id = "jFy7POPl8b4&t"  # Example live chat ID, replace with actual one

def get_live_chat_messages(live_chat_id):
    messages = []
    
    response = youtube.liveChatMessages().list(
        liveChatId=live_chat_id,
        part='id,snippet,authorDetails',
        maxResults=200
    ).execute()

    while response:
        for item in response.get('items', []):
            message = item['snippet']['displayMessage']
            author = item['authorDetails']['displayName']
            published_at = item['snippet']['publishedAt']
            message_type = item['snippet']['type']

            # Checking if the message is a regular message or a reply
            if message_type == "textMessageEvent":
                messages.append([author, message, published_at, ''])

            # Check for replies
            if 'replies' in item['snippet']:
                replies = item['snippet']['replies']
                for reply in replies:
                    reply_author = reply['authorDetails']['displayName']
                    reply_message = reply['snippet']['displayMessage']
                    reply_published_at = reply['snippet']['publishedAt']
                    messages.append([reply_author, reply_message, reply_published_at, message])

        # Check if there is a nextPageToken to continue fetching
        if 'nextPageToken' in response:
            response = youtube.liveChatMessages().list(
                liveChatId=live_chat_id,
                part='id,snippet,authorDetails',
                pageToken=response['nextPageToken'],
                maxResults=200
            ).execute()
        else:
            break

        # Wait to avoid hitting rate limits
        time.sleep(1)

    return messages

# Fetch live chat messages
chat_messages = get_live_chat_messages(live_chat_id)

# Save to a CSV file
df = pd.DataFrame(chat_messages, columns=['Author', 'Message', 'Published At', 'Parent Message'])
df.to_csv('liveChatMessages.csv', index=False)

print("Successful! Check the CSV file that you have just created.")
