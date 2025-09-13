
from collections import Counter
import re

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    counts = Counter(words)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts

if __name__ == "__main__":
    
    text = "This is a sample text. This text is for counting word frequency. Word word word frequency frequency."
    frequencies = word_frequency(text)
    
    for word, count in frequencies:
        print(f"{word} → {count}")
