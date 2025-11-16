from googletrans import Translator
import csv
#from retrying import retry

#@retry(wait_fixed=2000, stop_max_attempt_number=3)
def translate_hindi_comments(csv_file, output_file):
    translator = Translator()
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    translated_rows = []
    for row in rows:
        translated_row = []
        for comment in row:
            try:
                translated_comment = translator.translate(comment, src='hi', dest='en').text
                translated_row.append(translated_comment)
            except Exception as e:
                print(f"Error translating comment: {e}")
                translated_row.append("")  # Append empty string if translation fails
        translated_rows.append(translated_row)
    
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(translated_rows)

# Example usage:
translate_hindi_comments('YoutubeComments.csv', 'translated_comments.csv')
