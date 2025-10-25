with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

letters = sum(ch.isalpha() for line in lines for ch in line)
words = sum(len(line.split()) for line in lines)
lines_count = len(lines)

print("Input file contains:")
print(f"{letters} letters")
print(f"{words} words")
print(f"{lines_count} lines")
