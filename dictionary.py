from PyDictionary import PyDictionary

dictionary = PyDictionary
word = input("Enter a word: ")

print(dictionary.meaning(word))
print("\n")
print(dictionary.synonym(word))
print("\n")
print(dictionary.antonym(word))
