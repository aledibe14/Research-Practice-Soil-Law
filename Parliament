import re
import fitz
from collections import Counter

words_to_count = ["shall", "should", "must", "may", "might", "have to", "could"]

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf_document:
        for page in pdf_document:
            text += page.get_text()
    return text

def count_words(text, words):
    text = text.lower()
    word_counts = Counter()
    for word in words:
        pattern = r'\b' + re.escape(word) + r'\b'
        word_counts[word] = len(re.findall(pattern, text))
    return word_counts

# Path to the PDF file
pdf_path = r"C:\Users\Gebruiker\Desktop\EU regulations\www.europarl.europa.eu.pdf"

# Estract and count words
text = extract_text_from_pdf(pdf_path)
counts = count_words(text, words_to_count)

for word, count in counts.items():
    print(f"'{word}': {count} occurrences")

# Calculate the value of x
num_obb = counts["shall"] + counts["have to"]
sum_other_words = sum(counts[word] for word in words_to_count)

# Avoid division by zero by adding a conditional check
if sum_other_words == 0:
    print("The sum of the occurrences of 'should', 'may', and 'might' is zero. Cannot divide by zero.")
    x = None
else:
    x = num_obb / sum_other_words

print(f"\nValue of x: {x}")
