# # Exercise 1: Storing String
# # Create a variable that stores your name and display it.
name = "Barsha"
print(name)
# # Store text I'm learning Python in a variable and display it.
text_1= "I'm learning python"
print(text_1)
# # Store text Ram said, "I've a pen." in a variable and display it.
text_2 = 'Ram said, "I\'ve a pen."'
#print(text_2)

# # Store below text in a variable (as multiline) and display it.
# # Dear Manager,
# # I am on leave!
# # Thanks
text_message = '''Dear Manager, 
                I am on leave!
                 Thanks'''     
print(text_message)

# # Store \n and \t are special character. We use \ to escape in a variable and display it.
Text_3 = "\\n and \\t are special characters."
print(Text_3)


# Exercise 2: Indexing and Slicing
# Create a variable my_str that stores We are learning Python and it's fun! and
# Find and display the first character.
my_str = "We are learning Python and it's fun!"
print(my_str) 
# Find and display the character at index 8.
print(my_str[8])

# Find and display the last character (using negative indexing).
print(my_str[-1])
# Find word Python using slicing and display it.
print(my_str[16:22])
# Find word fun using negative slicing and display it.
print(my_str[-4:-1])
# Find text lrn (i.e. only some part of text learning) and display it.
print(my_str[7:15:3])

# Reverse the string and display it.
#print(my_str[-29:-21])
print(my_str[::-1])
# Find sub-string that lies from 5th index till end and display it.
print(my_str[5:])
# Find sub-string that lies from start till 10th index and display it.
print(my_str[10:])


# Exercise 3: Generic functions
# Create a variable str_1 that stores Hello, str_2 that stores World and:
# Display HelloWorld by concatenating both strings.
str_1 = 'Hello'
str_2 = 'World'
print (str_1 + str_2)
# Assign greetings variable as Hello World by concatenating both strings and display it.

greetings = str_1 + " " + str_2
print(greetings)
# Assign my_str as HelloHelloHello using str_1 repetition.
my_str = str_1 * 3
print(my_str)
# Find and display number of characters in string my_str.
print(len(my_str))
# Change value of greetings variable to uppercase and display it.
print(greetings.upper())
# Change value of greetings variable to lowercase and display it.
print(greetings.lower())
# Change value of greetings variable to title case and display it.
print(greetings.title())
# # Swap the case of characters in greetings variable and display it.
print(greetings.swapcase())