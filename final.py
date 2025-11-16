# DqH_4uJ2BOI         426 comments of shorts                           good
# v=l_xzUJebu_Q       3285 you tube vedio comments valuenternainment   good
#  v=OP5Tvq-Cp2M&t=1s 2360 comments Abhi nad niyu
#  v=Z1U9CS8Z-2U      150 comments AI Jazeera English                  good
#  v=l37XiBGV3fE&t=122s 3754 comments The Deshbhakt
# v=rkytqnZgEmc         153 Entrprice mangement                        good
# v=R2meHtrO1n8         3203 Rishi Sunak                               leave 
# v=kvTVYJCmfq0&t=2s    235 Firstpost                          good

import pandas as pd
from apiclient.discovery import build


#api_key = "AIzaSyCTKc74mVIcWYDkrYg-Ync6K-wpRNyw4Og"  # Replace this dummy API key with your own.
api_key ="AIzaSyAnymtPKd2YnvSZTR3t1NE154uhua4AVeA"

youtube = build('youtube', 'v3', developerKey=api_key)

# List of video IDs to process
#video_ids = ["YqKYpgZ9FWU" , "hAk62lIhPic","6tGqzzmuyZ8" ,"YvmcSn5lnxM"]  # Replace with your video IDs "AXkZRJNkOq8", "gTo-lPOGPdg",

video_ids = ["DqH_4uJ2BOI" , "Z1U9CS8Z-2U","kvTVYJCmfq0" ,"l_xzUJebu_Q"]  # Replace with your video IDs "AXkZRJNkOq8", "gTo-lPOGPdg",

def scrape_comments(video_id):
    comments_data = []

    def extract_comments(data, video_id):
        for item in data["items"]:
            top_comment = item["snippet"]['topLevelComment']["snippet"]
            comment_id = item["snippet"]['topLevelComment']["id"]
            name = top_comment["authorDisplayName"]
            comment = top_comment["textDisplay"]
            published_at = top_comment['publishedAt']
            likes = top_comment['likeCount']
            replies = item["snippet"]['totalReplyCount']
            comments_data.append([name, comment, published_at, likes, replies, video_id, ''])
            
            if replies > 0:
                fetch_replies(comment_id, video_id)

    def fetch_replies(parent_id, video_id):
        replies_data = youtube.comments().list(part='snippet', maxResults='100', parentId=parent_id, textFormat="plainText").execute()
        for item in replies_data["items"]:
            reply = item["snippet"]
            name = reply["authorDisplayName"]
            comment = reply["textDisplay"]
            published_at = reply['publishedAt']
            likes = reply['likeCount']
            replies = ""
            comments_data.append([name, comment, published_at, likes, replies, video_id, parent_id])

        while "nextPageToken" in replies_data:
            replies_data = youtube.comments().list(part='snippet', maxResults='100', parentId=parent_id, pageToken=replies_data["nextPageToken"], textFormat="plainText").execute()
            for item in replies_data["items"]:
                reply = item["snippet"]
                name = reply["authorDisplayName"]
                comment = reply["textDisplay"]
                published_at = reply['publishedAt']
                likes = reply['likeCount']
                replies = ""
                comments_data.append([name, comment, published_at, likes, replies, video_id, parent_id])

    data = youtube.commentThreads().list(part='snippet', videoId=video_id, maxResults='100', textFormat="plainText").execute()
    extract_comments(data, video_id)

    while "nextPageToken" in data:
        data = youtube.commentThreads().list(part='snippet', videoId=video_id, pageToken=data["nextPageToken"], maxResults='100', textFormat="plainText").execute()
        extract_comments(data, video_id)

    return comments_data

# Collect comments from all specified video IDs
all_comments = []
for video_id in video_ids:
    all_comments.extend(scrape_comments(video_id))

# Save to a CSV file
df = pd.DataFrame(all_comments, columns=['Name', 'Comment', 'Time', 'Likes', 'Reply Count', 'Video ID', 'Parent ID'])
df.to_csv('ExtractAi.csv', index=False)

print("Successful! Check the CSV file that you have just created.")
