import csv
import emoji

def preprocess_comments(csv_file, output_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    updated_rows = [[emoji.demojize(item) for item in row] for row in rows]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

# Example usage:
preprocess_comments('ExtractAiComment.csv', 'emojiRemoveAicomment.csv')










#Ensure that your CSV file has a column named 'comment' 
'''import csv
import emoji

def preprocess_comments(csv_file, output_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    for row in rows:
        comment = row['comment']
        updated_comment = emoji.demojize(comment)
        row['comment'] = updated_comment
    
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows) '''

# Example usage:
#preprocess_comments('YoutubeComments.csv', 'preprocessed_comments.csv')
#preprocess_comments('YoutubeComments.csv', 'YoutubeComments.csv')

#If your CSV file doesn't have a header row and the comments are directly in each line without column names, you can modify the code to handle this scenario. You can read the CSV file without assuming a header row and access the comments directly by index.
