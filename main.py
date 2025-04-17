from stats import count_words, count_characters, transform_in_list
import sys

def get_book_text(filepath):
    content =""
    with open(filepath) as f:
        content = f.read()
    return content


def main():
  
  args = sys.argv
  print("args",args)
  if len(args) < 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

  book_path = args[1]
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {count_words(get_book_text(book_path))} total words")
  print("--------- Character Count -------")

  chars = count_characters(get_book_text(book_path))
  listed =  transform_in_list(chars)

  for dic in listed:
     
     if dic["character"].isalpha():
        print(f"{dic["character"]}: {dic["count"]}\n")

  print("============= END ===============")

main()