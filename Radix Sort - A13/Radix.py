#  File: Radix.py
#  Description: Radix Sort
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 4/2/21
#  Date Last Modified: 4//21

import sys


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue if empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


# Helper function to return a list with characters changed to index and trailing zeros
def helper_radix(str, index):
    if len(str) <= index:
        return 0
    # check if string at indx are all alphabetical letters
    elif str[index].isalpha():
      #Use ord() to use Unicode
        return ord(str[index]) - 87
    else:
        return int(str[index])


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort(a):
    #Find the max_length of the string
    max_length = 0
    for i in range(len(a)):
        if max_length < len(a[i]):
            max_length = len(a[i])

    bins = [Queue() for i in range(37)]

    #Place string a in Queue bin 10
    count = 0
    while bins[36].size() < len(a):
        bins[36].enqueue(a[count])
        count += 1
    # go through the index from the back
    index = max_length - 1
    while index >= 0:
        # go through the list and put them in according queue
        while bins[36].size() > 0:
            new_string = bins[36].dequeue()
            #Call the helper function
            bin_num = helper_radix(new_string, index)
            bins[bin_num].enqueue(new_string)
        # put everything back in bin 36
        for i in range(36):
            while bins[i].size() > 0:
                new_string = bins[i].dequeue()
                bins[36].enqueue(new_string)
        index -= 1
    # put the bin[36] into a result list
    res = []
    while bins[36].size() > 0:
        new_string = bins[36].dequeue()
        res.append(new_string)
    return res


def main():
  # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int(line)

    # create a word list
    word_list = []
    for i in range(num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append(word)

    # print word_list
    #print(word_list)

    # use radix sort to sort the word_list
    sorted_word_list = radix_sort(word_list)

    # print the sorted_list
    print(sorted_word_list)


if __name__ == "__main__":
    main()
