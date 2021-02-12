days_late = 15
in_demand = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a conditional that decides the amount of a library fine
#based on an overdue book. The fine is 1 dollar per day late
#for the first 10 days, and 2 dollars per day for every day
#after that. If the book is considered an "in demand" book,
#the fine is doubled.
#
#Print the cost of the library fine, including a dollar sign.
#If the book is not late, print $0.
#
#Under the original values above, this should print $40:
#$10 for the first 10 days late, $10 for the next 5 days late,
#and doubled because the book is in demand.


#Add your code here! Make sure to print the dollar sign, too.
cost = 0
sub = 0
if days_late <= 10:
    cost = days_late
    if in_demand is True:
        print('$' + str(cost * 2))
    else:
        print('$' + str(cost))

if days_late > 10:
    sub = days_late - 10
    cost = (sub * 2) + 10
    if in_demand is True:
        print('$' + str(cost * 2))
    else:
        print('$' + str(cost))


