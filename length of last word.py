def length_of_last_word(s):
    # Strip trailing spaces to ensure the split doesn't include empty last elements
    trimmed_s = s.rstrip()
    # Split the string into words
    words = trimmed_s.split()
    # The last word is the last element of the list
    last_word = words[-1]
    # Return the length of the last word
    return len(last_word)

user_input = input("please enter the word:")

print("the length of last word:", length_of_last_word(user_input))
 