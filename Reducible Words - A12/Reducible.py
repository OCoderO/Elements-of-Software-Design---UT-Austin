#  File: Reducible.py
#  Description:
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created:3/30/2021
#  Date Last Modified: 4/4/2021

import sys

# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime(n):
    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that
# string
def step_size (s, const):
    step = const - (hash_word(s, const))
    return step



# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word (s, hash_table):

  #initial position that the word can be in from hashing
  position = hash_word(s, len(hash_table))

  #if the spot is not empty, then we proceed to see if there is another empty spot within the list for the word
  if (hash_table[position] != ''):
    new_position = step_size(s, 13)

    #while the spot is not empty we will continue to increment our algorithm until we find a new spot for the word
    count = 0
    while (hash_table[(position + new_position *count) % len(hash_table)] != ''):
     count += 1

    #once we find a spot that is empty, we will assign the word to that spot
    hash_table[(position + new_position *count) % len(hash_table)] = s

  #if the initial spot is empty, we will place the word in that spot
  else:
    hash_table[position] = s


# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word (s, hash_table):
    hash_idx = hash_word(s, len(hash_table))
    if hash_table[hash_idx] == s:
        return True
    else:
        step = step_size(s, 13)
        double_hash_idx = hash_idx + step
        if double_hash_idx >= len(hash_table):
            double_hash_idx = double_hash_idx % len(hash_table)
        if hash_table[double_hash_idx] == s:
            return True
        else:
            while hash_table[double_hash_idx] != '':
                double_hash_idx += step
                if double_hash_idx >= len(hash_table):
                    double_hash_idx = double_hash_idx % len(hash_table)
                if hash_table[double_hash_idx] == s:
                    return True
    return False

#recursively finds if a word is reducible, if the word is
#reducible it enters it into the hash memo and returns True
#and False otherwise
def is_reducible (s, hash_table, hash_memo):
  #Check if string is 1 character and if that character is a word
  if(len(s) == 1):
      if(s == "a" or s == "i" or s == "o"):
          return(True)
      return(False)

  #Check find_word
  elif(find_word(s, hash_memo)):
      return(True)

  #Check find_word
  elif(find_word(s, hash_table)):
      for i in range(len(s)):
          #Temp is a temporary variable for the reduced word
          temp = s[:i] + s[i + 1:]
          if(is_reducible(temp, hash_table, hash_memo)):
              insert_word(s, hash_memo)
              return(True)
  else:
      return(False)

# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words (string_list):
    #variables to hold longest words
    longest_word = ''
    long_words_list = []

    for i in range(len(string_list)):
        #Check if the word to the right is longer than current longest word
        if len(string_list[i]) > len(longest_word):
            longest_word = string_list[i]
            long_words_list = []        #empty the list
            long_words_list.append(longest_word)
        #Add longest word to long_words_list
        elif len(string_list[i]) == len(longest_word):
            long_words_list.append(string_list[i])
    return long_words_list

def main():
  # create an empty word_list
  word_list = []

  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  # find length of word_list
  word_list_length = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  prime_N = 2 * word_list_length
  while is_prime(prime_N) == False:
      prime_N += 1

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for i in range(prime_N):
      hash_list.append('')

  
  

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for i in range(word_list_length):
      insert_word(word_list[i], hash_list)

  #print("Completed")
  # create an empty hash_memo
  hash_memo = []
    
  # # create an empty hash_memo of size M
  # # we do not know a priori how many words will be reducible
  # # let us assume it is 10 percent (fairly safe) of the words
  # # then M is a prime number that is slightly greater than 
  # # 0.2 * size of word_list
  size_M = int(0.2 * word_list_length)
  while is_prime(size_M) == False:
    size_M +=1
    

  # # populate the hash_memo with M blank strings

  for i in range(size_M):
    hash_memo.append('')
  insert_word('a', hash_memo)
  insert_word('i', hash_memo)
  insert_word('o', hash_memo)
  #print(hash_memo)

  # # create an empty list reducible_words
  reducible_words = []

  # # for each word in the word_list recursively determine
  # # if it is reducible, if it is, add it to reducible_words
  # # as you recursively remove one letter at a time check
  # # first if the sub-word exists in the hash_memo. if it does
  # # then the word is reducible and you do not have to test
  # # any further. add the word to the hash_memo.
  for i in range(word_list_length):
    if is_reducible(word_list[i], hash_list, hash_memo):
      reducible_words.append(word_list[i])

  #print(reducible_words)
  #print(hash_memo)

  # # find the largest reducible words in reducible_words
  long_words_list = get_longest_words(reducible_words)

  # # print the reducible words in alphabetical order
  # # one word per line
  long_words_list.sort()
  for i in range(len(long_words_list)):
    print(long_words_list[i])
  

if __name__ == "__main__":
  main()