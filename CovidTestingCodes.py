# People taking a Covid test need to have a sample taken, and this sample must be tracked to ensure that it doesn’t get confused with others. However, to protect the person’s privacy, the user’s details should be encrypted.

# Write a program which accepts two strings: Firstly, the person’s name to be encoded, and secondly, a sufficient amount of keytext (agreed with by the senior clinic staff but not known to anyone else). The name and keytext will be in telegram style, strictly in uppercase with no punctuation or spaces. Encode the name as follows:

# Each character of the keytext should be converted to a number in the range 0...25, such that ‘A’ is 0, ‘B’ is 1 and so on.
# Each keytext number should be added to the corresponding letter of the name to produce the encoded name, such that ‘A’ + 0 is ‘A’, ‘A’ + 1 is ‘B’, and so on.
# The addition wraps around after ‘Z’, such that ‘Y’ + 1 is ‘Z’, ‘Y’ + 2 is ‘A’, and so on.
# For each character of the name, print a line of output giving the character to be encoded, the keytext number (0..25), and then the resulting encoded character, separated by spaces.

# First sample session with the program using a keytext of just the letter A:

# Name?    RACHELLE
# Keytext? AAAAAAAA
# R 0 R
# A 0 A
# C 0 C
# H 0 H
# E 0 E
# L 0 L
# L 0 L
# E 0 E
# ​
# Second sample session with the program using a keytext of just the letter B:

# Name?    RACHELLE
# Keytext? BBBBBBBB
# R 1 S
# A 1 B
# C 1 D
# H 1 I
# E 1 F
# L 1 M
# L 1 M
# E 1 F
# ​
# Third sample session with the program, with a keytext of different letters:

# Name?    RACHELLE
# Keytext? ABCDEFGH
# R 0 R
# A 1 B
# C 2 E
# H 3 K
# E 4 I
# L 5 Q
# L 6 R
# E 7 L
# ​
# Hint: To create a complex program such as this one, you will need to apply a process of development in which you add each feature gradually. A suggested strategy would be as follows:

# Start with a program that just prints the message one character per line (the first column of output). Run this to make sure that it works correctly.
# Then, make your program do the same thing, but by taking the ASCII code of the character and then converting the ASCII code back to a character.
# Then, make it also calculate and print the keytext number (the second column of output), make sure this also works correctly, and so on.





#Function for keytext.
def alpha():
    alphabet = {}
    # Set the value of character by subtracting them by their ASCII.
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        value = ord(letter) - ord('A')
      # Store the output in the dictionary.
        alphabet[letter] = value
   
    return alphabet

# open the function.
key_function = alpha()
name = input("Name?    ").upper()
keytext = input("Keytext? ")
# separate the keytext input by characters.
keytext2 = [char for char in keytext]

index = 0
for naam in name:
    key_value = key_function[keytext2[index]]
    # R = 82 - 65 + 2 = 
    naam_value = (ord(naam) - ord('A') + 
    key_value) + ord('A')
    print(f"{naam} {key_value} {chr(naam_value)}")
    index += 1
    # The index wraps if it exceed the length of keytext.
    if index == len(keytext2):
      index = 0



