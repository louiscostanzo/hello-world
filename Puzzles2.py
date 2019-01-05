import math


# puzzles from the book ' Think Like a Programmer (the book uses C++)'
# puzzle 1 - using only two output statements, produce half of a square of hash symbols
# puzzle 2 - Luhn Checksum validation
# The luhn formula works as follows -
# using the original number, double the value of every other digit, starting from the rightmost digit
# then, add the values of the individual digits together - if a doubled value is now a two-
# digit number, add the digits together individually
# the ID number is valid if the sum is divisible by 10 - we will generate check digits later

# write a program that takes a non-stored ID number of arbitrary length and checks for luhn validation
#each character must be processed before reading the next one
#okay, I'm not sure how to ensure the number is not stored is an object
# so for a number such as 176248, we will generate a check digit
# the check digit will become the rightmost value, so- we get 1d(7)6d(2)4d(8)C
#C must be a single digit remember that we start from the rightmost digit, including C
# where C is the check digit and d() will be our double function
# we now get 11464416C so 1+1+4+6+4+4+1+6+C  = a number divisible by 10
# 27 + C = any number divisible by 10
# C will be 3
# our final number is 1762483

# one difficulty is that we will be processing digits as they are typed, and we need to know
# every other digit from right to left, not left to right
#next, a doubled number must have its individual digits summed
# we must determine when we have read the entire number
#and we need to figure out how to read the number digit by digit
# C++ has some differences in inputs as far as I know, so here's my version
# we start by addressing the digit doubling problem with one digit

def double_digit_sum (digit):
    doubled_digit  = int(digit)*2
    if (doubled_digit >= 10):
        sum_digits = 1+(doubled_digit % 10)
    else:
            sum_digits = doubled_digit
    return sum_digits
#digit = input('Enter a single digit number 0-9:')
#print ('Here is your sum',double_digit_sum(digit))
#note I included int(digit) within the function, we may be taking in strings
#we need not fear getting hex values for the strings representing an int input
#okay, let's try this with a number of a known length - 6
#let's also decide that this number won't need any doubling
#all we will do is read the digits, sum them, and check if the sum is divisible by 10
##number = str(input('Enter a six-digit number'))
##checksum = 0
##for obj in number:
##    checksum += int(obj)
##if (checksum % 10 == 0):
##    print ('Checksum is divisible by 10, it is valid')
##else:
##    print('Checksum is not divisible by 10, it is not valid')
##
#print('Checksum = ', checksum)
#great, we convert the input to a string, iterate through it, and add up the items into a checksum
#now we need a way to return every other digit, starting from the right
#with a list, we can return the last item with list[-1], let's try it
#print ('Last number',number[-1])
#great, now can we get the index of that number?
#print('wrong Index of last number',number.index(number[-1]))
#actually, that won't work in the case of a double number e.g. 123123
#let's try reversing the number and working from there?
#nope, strings cannot be reversed
number = str(input('Enter a number: '))
def index_of_last_digit(string):
    position = -1
    for item in string:
        position += 1
    return position
#print('Index of last number',index_of_last_digit(number))
# great now we have the correct index of the last digit from the input
def checksum(number):
    counter = index_of_last_digit(number)
    # this counter determines when we have reached the final digit
    number_sum = 0
    odd_even = 1
    while counter >= 0:
            #print('counter',counter)
            # this counter allows us to get every other number, starting at the last digit
            if odd_even % 2 == 0:
                print('doubling',number[counter])
                number_sum += double_digit_sum(number[counter])
                odd_even += 1
                counter -= 1
                print('running sum',number_sum)
            else:
                    #dont double the digit, but still add it
                print ('not doubling',number[counter])
                number_sum += int(number[counter])
                odd_even += 1
                counter -= 1
                #print('I_C:',odd_even)
                print('running sum', number_sum)
    return number_sum
#so that gets us a checksum
Variable = checksum(number)
if Variable % 10 == 0:
    print('Checksum is divisible by 10, it is valid - it is:', Variable)
else:
    print('Checksum is not divisible by 10 it is invalid - it is:', Variable)

##X= index_of_last_digit(number)
##while X >= 0:
##    print ('index-', X)
##    X -= 1
# okay, after all the testing, we are close to a luhn checksum validator
# 123456 -> 1+d(2)+3+d(4)+5+d(6) -> 1+4+3+8+5+1+2 = 24, l ->r, wrong direction
# 123456 -> d(1)+2+d(3)+4+d(5)+6 -> 2+2+6+4+1+0+6 = 21 - so our validator works for this case
# 12345 -> 1+d2+3+d4+5 -> 1+4+3+8+5 = 21
# # lets try 1762483 -> -> 30
