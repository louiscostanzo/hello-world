import math
import string

## From 'Think Like a Programmer'
##This puzzles involves decoding a message, the message is encoded as a stream of characters
##It contains comma-delimited integers, all positive, and all int type
##The character represented by the integer depends on the 'decoding mode'
##These modes are: 'uppercase' 'lowercase' and 'punctuation'
##In uppercase mode, each int represents an uppercase letter
##int mod 27 indicates the letter of the alphabet (1 = A, etc)
##so, uppercase 143 results in 143 mod 27 -> 8 -> H
##lowercase does the same with lower case letters
##lowercase 56 -> 56 mod 27 -> 2 -> b
##in punctuation mode we use int mod 9
##so 19 -> 19 mod 9 = 1 -> punctuation given by the table in the book
##
##                so we will create lists of uppercase and lowercase characters, and input
##                the punctuation list
##the message starts in uppercase mode
##each time the mod operation results in 0, the mode switches
##uppercase -> lowercase -> punctuation -> uppercase again
# we need to do the following
#read to the end of a string of characters
## this is difficult with C++'s cin.get() function, as we only get one character at a time
## python could do:
#               import sys
#               inputs= sys.stdin.read()
#  but thats a way to increase complexity
#for char in string:
#convert those characters to ints for safety
#int(char)
#convert each int into a character
## decode(int)
#add that character to a new string
# string + string
#track the decoding mode
#decoding mode = [0,1,2]
#let's check our ascii values using ord() and chr()
# also, we must note that any time the mod == 0, we only change the mode, there should be no output
#okay, the mod operation needs to be dependent on mode in order to check if X mod Y == 0
##print('A:',ord('A')) #upper case values start at 65
##print('a:',ord('a')) #lower case values start at 97
##print('":', ord('"'))
##print("':", ord('"')) #this is the hard part
#defining variables
decoding_mode = 0
Punctuation_Table = ['!','?',',','.'," ",';',"'",'"']
Decoded_Message = 'Decoded Message:'
#defining functions
def conditional_modulo(X):
        if decoding_mode == 0 or decoding_mode == 1:
                Y = X % 27
        else:
                Y = X % 9
        return Y

def decode (item): # decode checks the decoding mode and looks up the character, it will not iterate the decoding mode
    int (item)
    if    decoding_mode == 0:
        mod_item = item % 27
        decoded_char = chr(mod_item+ord('A')-1)
        #print('mod_item', mod_item)
        #print('mode 0 decoded_char', decoded_char)
    elif    decoding_mode == 1:
        mod_item = item % 27
        decoded_char = chr(mod_item+ord('a')-1)
        #print('mod_item', mod_item)
        #print('mode 1 decoded_char', decoded_char)
    else:
        mod_item = item % 9
        decoded_char = Punctuation_Table[mod_item-1]
        #print('mod_item', mod_item)
        #print('mode 2 decoded_char', decoded_char)
    return decoded_char
        

def iterate_decoding_mode (): #there must be a better way to do this. But for now, the decoding mode runs through 0,1,2 and back as it iterates
    global decoding_mode
    if decoding_mode <=1:
        decoding_mode += 1
    else:
            if decoding_mode == 2:
                decoding_mode = 0
    return

# code body
comma_seperated_string_of_digits = input('input a string of digits, split only by commas: ') # brings in a string of digits, seperated by commas
list_of_digits = comma_seperated_string_of_digits.split(',') #splits this string into a list of string digits

list_of_ints = [int(char) for char in list_of_digits] # converts this list of string digits into a list of useable ints, rather than converting each item when it gets decoded
#print ('your list of ints: ', list_of_ints)
    
for item in list_of_ints: 
       # print ('decoding mode = ', decoding_mode)
        if conditional_modulo(item) == 0: #using our conditional function to fulfill the requirement that iteration and no return be conditional on mode, it only iteration when the condition is met
                iterate_decoding_mode()
        else:                                           #pass the first test, and we can go ahead and decode
                Decoded_Message = Decoded_Message + decode(item)

print(Decoded_Message)


