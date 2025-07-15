import string
from collections import Counter

# 💬 Ask the user for input
print("Welcome to Text Analyzer!")
text = input("Enter the text here:\n")

# 🧼 Clean text (replace punctuation with spaces)
translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
cleaned_text = text.translate(translator)

# 📊 Word count
words = cleaned_text.split()
word_count = len(words)

# 🔠 Character count (excluding spaces)
char_count = len(cleaned_text.replace(" ", ""))

# 📏 Line count
line_count = text.count('\n') + 1

# 🔁 Frequency analysis
word_freq = Counter(words)
most_common = word_freq.most_common()
top_count = most_common[0][1]
top_words = [word for word, count in most_common if count == top_count]

# 📋 Display the results
print("\nAnalysis Results:")
print(f"Total Words: {word_count}")
print(f"Total Characters (no spaces): {char_count}")
print(f"Total Lines: {line_count}")
print("Most Common Word(s):")
for word in top_words:
    print(f"'{word}' (used {top_count} times)")
