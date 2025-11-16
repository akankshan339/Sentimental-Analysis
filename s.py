from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv
import sys

if len(sys.argv) < 3:
    print("Usage: script.py <output_file_name> <video_id_1> <video_id_2> ... <video_id_n>")
    sys.exit(1)

output_file = sys.argv[1]
video_ids = sys.argv[2:]

yt_client = build(
   # "youtube", "v3", developerKey="AIzaSyBYtpYM6w0ubolYp5DVYxBlXhvmQvd_IpM"
    "youtube", "v3", developerKey="AIzaSyAnymtPKd2YnvSZTR3t1NE154uhua4AVeA"
)

def get_comments(client, video_id, token=None):
    try:
        response = (
            client.commentThreads()
            .list(
                part="snippet",
                videoId=video_id,
                textFormat="plainText",
                maxResults=100,
                pageToken=token,
            )
            .execute()
        )
        return response
    except HttpError as e:
        print(f"HTTP Error {e.resp.status}: {e.error_details}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

all_comments = []

for vid_id in video_ids:
    next_token = None
    while True:
        resp = get_comments(yt_client, vid_id, next_token)
        if not resp:
            break
        all_comments += [(vid_id, item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]) for item in resp["items"]]
        next_token = resp.get("nextPageToken")
        if not next_token:
            break

print(f"Total comments fetched: {len(all_comments)}")

with open(output_file, "w", newline="", encoding="utf-8") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Video ID", "Comment"])
    for comment in all_comments:
        csv_writer.writerow(comment)

print(f"Comments have been written to {output_file}")
