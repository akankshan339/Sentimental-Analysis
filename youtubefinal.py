api_key = "AIzaSyCTKc74mVIcWYDkrYg-Ync6K-wpRNyw4Og"  # Replace this dummy API key with your own.

from apiclient.discovery import build
import pandas as pd

youtube = build('youtube', 'v3', developerKey=api_key)

# List of video IDs to process
video_ids = ["hAk62lIhPic", "your_other_video_id_1", "your_other_video_id_2"]  # Replace with your video IDs

def scrape_comments(video_id):
    comments_data = []
    box = [['Name', 'Comment', 'Time', 'Likes', 'Reply Count', 'Video ID']]
    
    def extract_comments(data):
        for i in data["items"]:
            name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
            comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
            published_at = i["snippet"]['topLevelComment']["snippet"]['publishedAt']
            likes = i["snippet"]['topLevelComment']["snippet"]['likeCount']
            replies = i["snippet"]['totalReplyCount']
            comments_data.append([name, comment, published_at, likes, replies, video_id])
            
            # Process replies
            if replies > 0:
                parent = i["snippet"]['topLevelComment']["id"]
                data2 = youtube.comments().list(part='snippet', maxResults='100', parentId=parent, textFormat="plainText").execute()
                for i in data2["items"]:
                    name = i["snippet"]["authorDisplayName"]
                    comment = i["snippet"]["textDisplay"]
                    published_at = i["snippet"]['publishedAt']
                    likes = i["snippet"]['likeCount']
                    replies = ""
                    comments_data.append([name, comment, published_at, likes, replies, video_id])
    
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
df = pd.DataFrame(all_comments, columns=['Name', 'Comment', 'Time', 'Likes', 'Reply Count', 'Video ID'])
df.to_csv('sportsComments.csv', index=False)

print("Successful! Check the CSV file that you have just created.")
