consonants = list("BCDFGHJKLMNPQRSTVWXYZ")
vowels = list("AEIOU")
language_number = int(input("Language number for this session: "))

def encoder(word):
  word = list(word)
  for i in range(len(word)):
    if word[i] in consonants:
      word[i] = consonants[(i+language_number+(consonants.index(word[i])))%len(consonants)]
    elif word[i] in vowels:
      word[i] = vowels[(i+language_number+(vowels.index(word[i])))%len(vowels)]
  a.append(''.join(word))

def decoder(word):
  word = list(word)
  for i in range(len(word)):
    if word[i] in consonants:
      word[i] = consonants[((consonants.index(word[i]))-i-language_number)%len(consonants)]
    elif word[i] in vowels:
      word[i] = vowels[((vowels.index(word[i]))-i-language_number)%len(vowels)]
  a.append(''.join(word))

def processor(word_list, value):
  if value == 0:
    for i in word_list:
      encoder(i)
  elif value == 1:
    for i in word_list:
      decoder(i)

while(True):
  a = []
  word_list = list(map(list, input("Enter string: ").upper().split()))
  processor(word_list, 1) if input("Enter 1 for Decode, 0 for Encode: ") == "1" else processor(word_list, 0)
  print(" ".join(a))
