phrase = str(input("Give me a word or phrase, let's see if it's a palindrome!: "))
if phrase.lower() == phrase.lower()[::-1]:
    print("It's a palindrome!!!!")
else:
    print("No palindrome here!")