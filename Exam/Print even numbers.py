minimum = 5
maximum = 14

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write a loop (we suggest a for loop) that prints all the
#even numbers from minimum to maximum. Each number should be
#printed on its own line, and you should print both minimum
#and maxmimum themselves if they are even. You may assume
#minimum will always be less than maximum.
#
#With the initial values for minimum and maximum above, this
#should print 6, 8, 10, 12, 14 -- each number would be on its
#own line, no commas.


#Add your code here!
for i in range(minimum, maximum + 1):
    if i % 2 == 0:
        print(i)
