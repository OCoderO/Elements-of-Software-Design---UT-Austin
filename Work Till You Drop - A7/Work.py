#  File: Work.py
#  Description: Testing Linear Search and Binary Search
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 2/21/2021
#  Date Last Modified: 3/3/2021

import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series(v, k):
    ###The linear search (and binary search) function should return the minimum value of v that will allow Vyasa to write n lines of code before falling asleep, given n and k.
    ###test different values of v to find the smallest value that yields at least n lines of code
    ###test different values of v, whats the min
    # v/k next time
    # v/K**2
    # until v/k**n = 0
    total = 0
    i = 0
    while v // k ** i != 0:
        total += v // (k ** i)
        i += 1
    return total


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
# no real need to explicitly store it (not explicitly creating a list is just a space optimization and isn't necessary for the assignment). Do a forloop!

# In this case, finding the SMALLEST v that is LARGE enough to satisfy the condition

# where the sum of the series v + v // k + v // k**2 + ... >= n, then break from the binary search.
# Make sure to use **
# //(interger division)
# use in both searches, the total line of codes
# if output of sum series < n, keep searching
def linear_search(n, k):
    for v in range(n + 1):
        local_total = sum_series(v, k)
        if int(local_total) >= n:
            return v


# for loop to test v
# helper function tells you when to break and stop the entire search , break the loop


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor


# code should be log n time complexity, otherwise you are likely to time out on these tests.

def binary_search(n, k):
    left = 0
    right = n
    v = 0
    while right >= left:
        v = left + (right - left) // 2
        total = sum_series(v, k)
        if (total < n):
            left = v + 1
        elif (total > n):
            right = v - 1
        else:
            return v
    if sum_series(v, k) >= n:
        return v


##should return the number of lines Vyasa will write before falling asleep given v and k
##how many lines of code Vyasa writes for a specific value of v
# testing out different values of v, use this function to see if this the min
# use the helper function to see if it is the correct v


# Input: no input
# Output: a string denoting all test cases have passed

# def test_cases():
# write your own test cases
# return "all test cases passed"

def main():
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int(line)

    for i in range(num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp = line.split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


if __name__ == "__main__":
    main()
