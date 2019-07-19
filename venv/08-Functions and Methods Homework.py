# 1)
"""
Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as
43π𝑟3
"""
def vol(rad):
    return (4/3) * (3.14) * (rad**3)
    pass

print (vol(2))

#2)Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num > low and num < high:
        print(num, "is in the range of", low, "and", high)

print(ran_check(5,2,7))

#3)**Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    d = {"upper":0,"lower":0}
    for c in s :
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
print(up_low(s))

#4) Write a Python function that takes a list and returns a new list with unique elements of the first list
Sample_List : [1,1,1,1,2,2,3,3,3,3,4,5]
def unique_list(lst):
    x=[]
    for n in lst:
        if n not in x:
            x.append(n)
    return (x)
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

#5)Write a Python function to multiply all the numbers in a list
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
        print(total)
    return total
print(multiply([1,2,3,-4]))

#6)Write a Python function that checks whether a passed string is palindrome or not
def palindrome(c):
    c = c.replace(' ','')  # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return c == c[::-1]  # Check through slicing

print(palindrome("ABBA"))

#7)Write a Python function to check whether a string is pangram or not
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
print(ispangram("The quick brown fox jumps over the lazy dog"))
