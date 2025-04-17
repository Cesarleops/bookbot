
def count_words(text):
   words = text.split()
   return len(words)


def count_characters(text):

   char_count = {}
   for char in text:
      char = char.lower()
      if char not in char_count:
         char_count[char] = 1
      else:
         char_count[char]+=1
      
   return char_count

def sort_on(dict):
    return dict["count"]


def transform_in_list(dictionary):

    dictionaries = []

    for key in dictionary:
     dictionaries.append({
       "character": key,
       "count": dictionary[key]
     })

    dictionaries.sort(reverse=True, key=sort_on)
    return dictionaries
    