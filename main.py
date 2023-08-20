# Constants as string literals
CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZ"
VOWELS = "AEIOU"

# Decoder and encoder function, more concise and easier to manage
def transform_word(word, language_number, operation):
    transformed_word = []
    for i, char in enumerate(word):
        char_list = CONSONANTS if char in CONSONANTS else VOWELS if char in VOWELS else [char]
        index = (i + language_number + char_list.index(char)) % len(char_list) if operation == 0 else (char_list.index(char) - i - language_number) % len(char_list) if operation == 1 else i
        transformed_char = char_list[index % len(char_list)]
        transformed_word.append(transformed_char)
    return ''.join(transformed_word)

def process_word_list(word_list, language_number, operation):
    return [transform_word(word, language_number, operation) for word in word_list]

def main():
    while True:
        word_list = input("Enter string: ").upper().split()
        language_number = int(input("Language number for this session: "))
        operation = int(input("Enter 1 for Decode, 0 for Encode: "))
        
        processed_words = process_word_list(word_list, language_number, operation)
        print(" ".join(processed_words))

if __name__ == "__main__":
    main()