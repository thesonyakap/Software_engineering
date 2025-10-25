from collections import Counter

with open("article.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

words = [word.strip(".,!?;:-()«»\"'") for word in text.split()]
words = [w for w in words if w]

word_count = len(words)
most_common = Counter(words).most_common(1)[0]

print(f"Количество слов в файле: {word_count}")
print(f"Самое частое слово: '{most_common[0]}' — встречается {most_common[1]} раз(а)")
