text = input().lower().replace(".", "")
words = text.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

grouped_by_len = {}
for word in counts:
    length = len(word)
    grouped_by_len.setdefault(length, []).append(word)

print("Word Frequencies:")
for word, count in counts.items():
    print(f"{word}: {count}")

print("Grouped By Length:")
for length in sorted(grouped_by_len):
    print(f"{length}: {', '.join(grouped_by_len[length])}")
