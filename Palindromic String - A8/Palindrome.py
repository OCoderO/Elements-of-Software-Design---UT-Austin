#  File: Palindrome.py
#  Description:
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created:3/6/2021
#  Date Last Modified: 3/8/2021

import sys

## Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a boolean on whether the string is a palindrome or not
def isPalindrome(s):
    if s == s[::-1]:
        return True


# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    #Check if original str is already a palindrome
    if isPalindrome(str) == True: 
        return str
    else:
        for i in range(len(str)):
            if isPalindrome(str[:i]) == True: 
                root = str[:i]      #find the root of the palindrome
                suffix = str[i:]    #find the suffix  
        reverse = suffix[::-1]      #find the reverse of the suffix and add it to the beginning
        return reverse + root + suffix  #return the created palindrome

        

# Input: no input
# Output: a string denoting all test cases have passed
#def test_cases():
  # write your own test cases
  #return "all test cases passed"

def main():
    # run your test cases

    # read the data
    for line in sys.stdin.readlines():
        #Call smallest_palindrome and print out the output
        print(smallest_palindrome(line.strip()))
        

    

    # print the smallest palindromic string that can be made for each input

if __name__ == "__main__":
  main()