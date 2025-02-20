import argparse
from count_words import count_words

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Count words in a text.')
  parser.add_argument('--file', help='Text to count words in')
  parser.add_argument('text', nargs='?', help='Text to count words in')
  args = parser.parse_args()

  if args.file:
    with open(args.file, 'r') as f:
      text = f.read()
  elif args.text:
    text = args.text
  else: 
    print("Please provide either text or a file to count words in.")
    exit(1)

  print("Word count: {}".format(count_words(text)))