def count_words(text):
    words = text.split()
    count = len(words)
    print(f"Found {count} total words")
def count_characters(text):
    total = {}
    for ch in text:
        character = ch.lower()
        if character in total:
            total[character] += 1
        else:
            total[character] = 1
    print(total)