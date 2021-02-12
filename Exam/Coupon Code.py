#Write a function called find_final_price. find_final_price
#should have two positional parameters: a price and a sales
#tax rate. It should also have a keyword parameter called
#coupon_code, with a default value of 0.
#
#find_final_price should return the final price of the item,
#which is the initial price plus the sales tax (price times
#tax rate) minus the coupon code.
#
#Round the final answer to two decimal places. You can do
#that with final_price = round(previous_price, 2).


#Add your code here!
def find_final_price(price, sales_tax, coupon_code=0):
    final_price = 0
    tax = 0
    tax = price * sales_tax
    final_price = (price + tax) - coupon_code
    return  round(final_price, 2)




#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#10.70
#5.70
print(find_final_price(10.0, 0.07))
print(find_final_price(10.0, 0.07, coupon_code = 5.0))
