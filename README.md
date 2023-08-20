# Gibberish Generator Algorithm

This Python program allows you to encode and decode words based on a simple set of rules. The program utilizes consonants and vowels as well as a language number to transform input words.

## Key Features

- Advancing Caesar Cipher
- Separate for Vovels and Consonants
- Reusable and constant in sentences
- Good for Fantasy RPGs

I decided to update this because it may be incorporated [here](https://github.com/ozgurozbek/teothe/issues/17) and the code needed some QOL updates, especially readability and best practices. I also force-pushed to master after some squashing.

## Usage

1. Run the program.
1. Enter a list of words separated by spaces, a sentence one might say.
1. Provide a language number.
1. Choose an operation: 0 to encode or 1 to decode.
1. Get the transformed words as output.

## Functions

### Transformation Function

The transform_word function is the heart of the encoding and decoding process. It takes three parameters:

word: The input word to be transformed.
language_number: A number used for encoding/decoding.
operation: An integer representing the operation (0 for encode, 1 for decode).

The function then iterates through each character of the input word:
If the character is a consonant, it uses the CONSONANTS constant, if the character is a vowel, it uses the VOWELS constant, if the character is neither a consonant nor a vowel, it uses the character itself.

The index for transformation is calculated based on the rules:

- Encoding (0), `index = (original index + language number + character index) % character list length`.
- Decoding (1), `index = (character index - original index - language number) % character list length`.

### Word List Processing

The process_word_list function processes a list of words using the transform_word function. It takes three parameters:

word_list: A list of words to be transformed.
language_number: A number used for encoding/decoding.
operation: An integer representing the operation (0 for encode, 1 for decode).
It returns a list of transformed words.

### Main Loop

The main function serves as the entry point of the program. It contains a loop that repeatedly takes user input and processes it:

- The user is prompted to enter a list of words separated by spaces.
- The user provides a language number for the session.
- The user chooses an operation: 0 for encoding or 1 for decoding.
- The process_word_list function is then called to transform the input words according to the chosen operation. Transformed words are printed as output.
