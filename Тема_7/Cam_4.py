import re

with open("input.txt", "r", encoding="utf-8") as f:
    banned_words = f.read().split()

text = """Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!"""

for word in banned_words:
    pattern = re.compile(word, re.IGNORECASE)
    text = pattern.sub("*" * len(word), text)

print(text)
