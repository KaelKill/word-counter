import string

def count_words(text):
    formatted_text = remove_punctuation(text)
    return len(formatted_text.split())
    
def remove_punctuation(text):
    table = str.maketrans("", "", string.punctuation)
    return text.translate(table)