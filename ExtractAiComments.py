import pandas as pd
from apiclient.discovery import build

api_key = "AIzaSyAnymtPKd2YnvSZTR3t1NE154uhua4AVeA"

youtube = build('youtube', 'v3', developerKey=api_key)

# List of video IDs to process
video_ids = ["DqH_4uJ2BOI", "Z1U9CS8Z-2U", "kvTVYJCmfq0", "l_xzUJebu_Q"]  

def scrape_comments(video_id):
    comments_data = []

    def extract_comments(data):
        for item in data["items"]:
            top_comment = item["snippet"]['topLevelComment']["snippet"]
            comment = top_comment["textDisplay"]
            comments_data.append([comment])
            
            if item["snippet"]['totalReplyCount'] > 0:
                fetch_replies(item["snippet"]['topLevelComment']["id"])

    def fetch_replies(parent_id):
        replies_data = youtube.comments().list(part='snippet', maxResults='100', parentId=parent_id, textFormat="plainText").execute()
        for item in replies_data["items"]:
            reply = item["snippet"]
            comment = reply["textDisplay"]
            comments_data.append([comment])

        while "nextPageToken" in replies_data:
            replies_data = youtube.comments().list(part='snippet', maxResults='100', parentId=parent_id, pageToken=replies_data["nextPageToken"], textFormat="plainText").execute()
            for item in replies_data["items"]:
                reply = item["snippet"]
                comment = reply["textDisplay"]
                comments_data.append([comment])

    data = youtube.commentThreads().list(part='snippet', videoId=video_id, maxResults='100', textFormat="plainText").execute()
    extract_comments(data)

    while "nextPageToken" in data:
        data = youtube.commentThreads().list(part='snippet', videoId=video_id, pageToken=data["nextPageToken"], maxResults='100', textFormat="plainText").execute()
        extract_comments(data)

    return comments_data

# Collect comments from all specified video IDs
all_comments = []
for video_id in video_ids:
    all_comments.extend(scrape_comments(video_id))

# Save to a CSV file
df = pd.DataFrame(all_comments, columns=['Comment'])
df.to_csv('ExtractAiComment.csv', index=False)

print("Successful! Check the CSV file that you have just created.")
