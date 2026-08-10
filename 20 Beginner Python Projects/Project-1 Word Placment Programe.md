# Word Replacement Program

def replace_word():

```python
print("================================")
print("      WORD REPLACEMENT PROGRAM")
print("================================")

string = input("Enter your sentence: ")

word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the replacement word: ")

if word_to_replace in string:

    new_string = string.replace(word_to_replace, replacement_word)

    print("\nOriginal Sentence:", string)
    print("Word Replaced Successfully!")
    print("New Sentence:", new_string)

else:

    print("\nWord not found in the sentence!")
```

replace_word()

================================
      WORD REPLACEMENT PROGRAM
================================

Enter your sentence: This is Ishfaq Khan
Enter the word to replace: Ishfaq
Enter the replacement word: Python

Original Sentence: This is Ishfaq Khan
Word Replaced Successfully!
New Sentence: This is Python Khan
