from PyDictionary import PyDictionary

dictionary = PyDictionary
word = input("Enter a word: ")

print(dictionary.meaning(word))
print("")
print(dictionary.synonym(word))
print("")
print(dictionary.antonym(word))
