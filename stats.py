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
    return total
def sort_by_greatest(characters):
    sorted_list = []
    for character in characters:
        character_count = {}
        character_count["char"] = character
        character_count["count"] = characters[character]
        sorted_list.append(character_count)
    def get_count(list):
        return list["count"]
    sorted_list.sort(reverse = True, key = get_count)
    return sorted_list