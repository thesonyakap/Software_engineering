from collections import Counter

def analyze_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        words = [w.strip(".,!?;:-()«»\"'").lower() for w in f.read().split() if w]

    counter = Counter(words)
    unique = len(counter)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Всего слов: {sum(counter.values())}\n")
        f.write(f"Уникальных слов: {unique}\n")
        f.write("Топ-5 слов:\n")
        for w, c in counter.most_common(5):
            f.write(f"{w}: {c}\n")

    print(f"Статистика записана в файл {output_file}")

analyze_file("article.txt", "stats.txt")
