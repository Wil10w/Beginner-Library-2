the_string = "Ramblin"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#The string class has a method called islower which returns
#True if a string is all lower case, false if it is not.
#For example, if the_string = "Ramblin", then calling the
#method the_string.islower() would return False. If instead
#the_string was "wreck", the_string.islower() would return
#True.
#
#Write some code that uses islower to print True if
#the_string is all lower case, False if it is not. However,
#if the_string isn't actually a string, this would instead
#cause an AttributeError. Catch that error and instead
#print the message "Only strings can be lowercase!".
#
#Note that you may not use any conditionals in your answer.
#Note also that you should not assume that every error that
#occurs is an attribute error: any other errors should not
#be caught.


#Add your code here!
try:
    trueOrFalse = None
    if the_string.islower():
        trueOrFalse = True
        print(trueOrFalse)
    else:
        if not the_string.islower():
            trueOrFalse = False
            print(trueOrFalse)
except AttributeError:
    print('Only strings can be lowercase')
