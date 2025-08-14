import json
import re

# def clean_sentence(sentence):
#     # Remove newlines and carriage returns
#     sentence = sentence.replace("\n", " ").replace("\r", " ")
#     # Remove specific Unicode characters (smart quotes, etc.)
#     sentence = sentence.replace("\u201c", "").replace("\u201d", "")
#     # Optionally remove em-dash and en-dash
#     sentence = sentence.replace("\u2014", " ").replace("\u2013", " ")
#     return sentence.strip()

def process_json(input_file, output_file):
    word_first_occurrence = {}  # word -> "BOOK CHAPTER:VERSE"

    with open(input_file, "r", encoding="utf-8") as f:
        bible_data = json.load(f)

    books = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther", "Job", "Psalm", "Proverbs", "Ecclesiastes", "Song Of Solomon", "Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"]

    for book, chapters in bible_data.items():
        book = books.index(book)

        for chapter, verses in chapters.items():
            for verse, sentence in verses.items():

                location = f"{book} {chapter}:{verse}"

                # Tokenize words (case-insensitive)
                words = re.findall(r"\b[\w']+\b", sentence)
                for word in words:
                    w_lower = word.lower()
                    if w_lower not in word_first_occurrence:
                        word_first_occurrence[w_lower] = location

    # Save output
    with open(output_file, "w", encoding="utf-8") as out:
        for word, location in sorted(word_first_occurrence.items()):
            out.write(f"{word} {location}\n")


# Example usage:
process_json("esv.json", "esv-out.txt")
