#Write a function called get_numerals. get_numerals should
#accept one parameter, a string. It should return a string
#containing only the numerals from the original string:
#no letters, punctuation marks, or spaces.
#
#Remember, numerals have ordinal numbers between 48 ("0")
#and 57 ("9"). You may use the ord() function to get
#a letter's ordinal number.
#
#Your function should be able to handle strings with no
#numerals (return an empty string) and strings with all
#numerals (return the original string). You may assume
#we'll only use regular characters (no emojis, formatting
#characters, etc.).


#Write your function here!
def get_numerals(a_string):
    # Variable to collect numbers from i
    output = ''

    for i in a_string:
        # iterating through a_string
        if i.isdigit():
            # if it's a number
            output += i
        # add the 'string number' to output
    return output


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#1301
#
#8675309
print(get_numerals("CS1301"))
print(get_numerals("Georgia Institute of Technology"))
print(get_numerals("8675309"))
