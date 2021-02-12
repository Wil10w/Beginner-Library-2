#Write a function called product_code_check. product_code_check
#should take as input a single string. It should return a boolean:
#True if the product code is a valid code according to the rules
#below, False if it is not.
#
#A string is a valid product code if it meets ALL the following
#conditions:
#
# - It must be at least 8 characters long.
# - It must contain at least one character from each of the
#   following categories: capital letters, lower-case letters,
#   and numbers.
# - It may not contain any punctuation marks, spaces, or other
#   characters.


#Add your code here!
def product_code_check(code):
    count = 0
    for num in code:
        count += 1
    if count >= 8:
        if code.isdigit():
            if code.islower();
                if code.isupper():


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, False
print(product_code_check("g00dlONGproductCODE"))
print(product_code_check("fRV53FwSXX663cCd"))
print(product_code_check("2shOrt"))
print(product_code_check("alll0wercase"))
print(product_code_check("inv4l1d CH4R4CTERS~"))



