import string

def text_analysis(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    uppercase_count = sum(1 for char in text if char.isupper())
    lowercase_count = sum(1 for char in text if char.islower())
    special_symbols_count = sum(1 for char in text if char in string.punctuation)

    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")
    print(f"Uppercase Letters: {uppercase_count}")
    print(f"Lowercase Letters: {lowercase_count}")
    print(f"Special Symbols: {special_symbols_count}")


file_path = 'sampletext.txt'
text_analysis(file_path)
