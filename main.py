# Define constants using string literals
CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZ"
VOWELS = "AEIOU"

def encoder(word, language_number):
    encoded_word = []
    for i, char in enumerate(word):
        if char in CONSONANTS:
            encoded_char = CONSONANTS[(i + language_number + CONSONANTS.index(char)) % len(CONSONANTS)]
        elif char in VOWELS:
            encoded_char = VOWELS[(i + language_number + VOWELS.index(char)) % len(VOWELS)]
        else:
            encoded_char = char
        encoded_word.append(encoded_char)
    return ''.join(encoded_word)

def decoder(word, language_number):
    decoded_word = []
    for i, char in enumerate(word):
        if char in CONSONANTS:
            decoded_char = CONSONANTS[(CONSONANTS.index(char) - i - language_number) % len(CONSONANTS)]
        elif char in VOWELS:
            decoded_char = VOWELS[(VOWELS.index(char) - i - language_number) % len(VOWELS)]
        else:
            decoded_char = char
        decoded_word.append(decoded_char)
    return ''.join(decoded_word)

def process_word_list(word_list, language_number, operation):
    processed_words = []
    for word in word_list:
        if operation == 0:
            processed_words.append(encoder(word, language_number))
        elif operation == 1:
            processed_words.append(decoder(word, language_number))
    return processed_words

def main():
    while True:
        word_list = input("Enter string: ").upper().split()
        language_number = int(input("Language number for this session: "))
        operation = int(input("Enter 1 for Decode, 0 for Encode: "))
        
        processed_words = process_word_list(word_list, language_number, operation)
        print(" ".join(processed_words))

if __name__ == "__main__":
    main()