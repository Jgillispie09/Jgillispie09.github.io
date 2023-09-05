print("Hello user! Let's find out if your entry is a palindrome!")
user_input = input("Enter a word or phrase!\n")
if user_input == user_input[::-1]:
    print("It's a palindrome!!")
else:
    print("It's not a palindrome!!")