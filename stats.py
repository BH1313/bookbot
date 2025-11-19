def count_words(text):
  words = text.split()
  return len(words)  

def count_character(text):
  counts = {}
  for char in text.lower():
    if char not in counts:
      counts[char] = 0
    counts[char] += 1
  return counts

def sort_character(characters):
  char_list = []
  for char, num in characters.items():
    char_list.append({"char": char, "num": num})

  def sort_key(item):
    return item["num"]

  char_list.sort(key=sort_key, reverse=True)
  return char_list

