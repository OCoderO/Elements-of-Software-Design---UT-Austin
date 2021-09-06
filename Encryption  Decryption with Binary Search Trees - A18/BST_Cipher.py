#  File: BST_Cipher.py
#  Description:
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 4/21/21
#  Date Last Modified: 4/23/21

import sys

class Node (object):
  # Constructor
  def __init__ (self, data = None, lChild = None, rChild = None):
    self.data = data
    self.lChild = lChild
    self.rChild = rChild
  
  # String representation  
  def __str__(self):
    return str(self.data)

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root = None
    self.estr = encrypt_str

    #Make the sure the encrypt_str is all lower case
    self.estr = self.estr.lower()
    correct = ''

    # creates an encryption key that only contains a-z and ' '
    for i in range (len(self.estr)):
      if ('a'<=self.estr[i] and self.estr[i]<='z') or (self.estr[i]==' '):
        correct += self.estr[i]
    self.estr = correct

    # creates the BST with the key
    for i in range (len(self.estr)):
      self.insert(self.estr[i])

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    newnode = Node(ch)

    if (self.root == None):
      self.root = newnode

    else:
      current = self.root
      parent = self.root
      while current != None:
        parent = current
        if ch == current.data:
          return
          
        if ch < current.data:
          current = current.lChild
        else:
          current = current.rChild

      if ch < parent.data:
        parent.lChild = newnode
      else:
        parent.rChild = newnode

  
  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    #Create a string to hold a series of lefts
  # (<) and rights (>) needed to reach that character
    result = ''
    #Create a variable current to keep track of where we are in the string
    current = self.root

    #return a blank string if the character does not exist in the tree
    if (current == None):
      return ''

    #return * if the character is the root of the tree.
    if self.root.data==ch:
      return '*'

    #Check if you have reached the end of the Tree OR you have found the character
    while (current != None) and (current.data != ch):
      if (ch < current.data):
        result += '<'
        current = current.lChild
      else:
        result += '>'
        current = current.rChild
    return result


  # the traverse() function will take string composed of a series of
 
  # character in the binary search tree. It will return an empty string
 
  def traverse (self, st):
    temp = self.root

    if (st == '*'):
      return temp.data
    else:
      for i in st:
        if temp == None:
          return ""
       # lefts (<) and rights (>) and return the corresponding 
        if (i == "<"):
          temp = temp.lChild
        elif (i == ">"):
          temp = temp.rChild
         # if the input parameter does not lead to a valid character in the tree.
        elif temp == None:
          return ""
    return temp.data


  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    #Check if the st is empty if so return an empty string
    if st == '':
      return ''
    
    #Converts st the string to lowercase
    st = st.lower()
    encrypt_stng =''
    
    for i in range (len(st)):
      if ('a'<=st[i] and st[i]<='z') or (st[i]==' '):
        # the search function will add the path to the encryption
        encrypt_stng += self.search(st[i])+'!'

        
    
    # based on sample output, the final delimiter is not included
    return encrypt_stng[:len(encrypt_stng)-1]

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    #Check if the st is empty if so return an empty string
    if st == '':
      return ''
    
    #Creates an empty string to hold the decryption
    output = ''
    
    #Split the encrypted string st at the !, this creates a list of strings
    st = st.split('!')
    
    #Traverse through the list of strings st
    for i in range (len(st)):
      output +=self.traverse(st[i])

    return output

def main():
  # read encrypt string
  line = sys.stdin.readline()
  encrypt_str = line.strip()

  # create a Tree object
  the_tree = Tree (encrypt_str)

  # read string to be encrypted
  line = sys.stdin.readline()
  str_to_encode = line.strip()

  # print the encryption
  print (the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
  line = sys.stdin.readline()
  str_to_decode = line.strip()
  
  # print the decryption
  print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
  main()

