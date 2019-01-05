import math


# puzzles from the book ' Think Like a Programmer (the book uses C++)'
# puzzle 1 - using only two output statements, produce half of a square of hash symbols
# soemthing like below:
#####
####
###
##
#

### reduce to whole square first
##
### reduce to a single line
##num = 0
##while (num <= 5):
##    print('#')
##    num += 1
### okay, python's print function puts each symbol on a new line
### we can still solve the problem and build up
##numB = 5
##print('#' * numB)
###next step i can think of is to see what happens in a while loop
##numC = 0
##while (numC <= 5):
##   print ('#' * numC)
##   numC += 1
### the above created an upside-down picture of what we need, let's flip it
##
###numD = 5
###while (numD <= 5):
###    print('#' * numD)
###    numD -= 1
### okay that works, but we are working with unterminated while loops here, let's not do that
##
for numE in range (6):
    print('#'*numE)
    numE += 1
# now all we need to do is flip it over, and we sure can
for numE in reversed(range(6)):
    print('#'*numE)
    numE += 1
    
    

