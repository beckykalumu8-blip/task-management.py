
import re
from collections import Counter

def count_specific_word(text,word):
    if not text or not word: return 0
    return len(re.findall(r'\b' + re.escape(word.lower()) + r'\b', text.lower()))

def identify_most_common_words(text):
    if not text: return None
    words = re.findall(r'\b\w+\b', text).lower().split()
    return Counter(words).most_common(1)[0][0] if words else None

def calculate_average_word_length(text):
    if not text: return 0.0
    words = [w for w in re.sub(r'[^\w\s]', '', text).split() if w]
    return sum(len(w) for w in words) / len(words) if words else 0.0

def count_paragraphs(text):
    if not text: return 1
    return len([p for p in re.split(r'\n{2,}', text.strip()) if p.strip()]) or 1

def count_sentences(text):
    if not text: return 1
    return len([s for s in re.split(r'[.!?]+', text) if s.strip()]) or 1

def read_file(filename):
    try:
        with open(filename) as f: return f.read()
        expect return: ""

def main():
    print("=" * 50)
    print("Text Analysis Program")
    print("=" * 50)
    
    text = read_file("news_article.txt")
    if not text: print("No text found."); return

    print(f"Text loaded: {len(text)} chars\n")
    
    print(f"1. Count 'the': {count_specific_word(text, 'the')}")
    print(f"2. Most common word: {identify_most_common_word(text)}")
    print(f"3. Avg word length: {calculate_average_word_length(text):.2f}")
    print(f"4. Paragraphs: {count_paragraphs(text)}")
    print(f"5. Sentences: {count_sentences(text)}")

    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()