#  File: Poly.py
#  Description:
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 4/13/21
#  Date Last Modified: 4/16/21

import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff #This will represent coefficient
    self.exp = exp     #This will represent the exponent
    self.next = next   #This will be the pointer which points to the next Link

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    #Before inserting into the linked list you must create a link
    new_link = Link(coeff, exp)
    #keeps track of where we are in the list
    current = self.first   
    
    #Check if the Linked List is empty
    if current == None:  
      self.first = new_link
      return
      
    #Check if exp > the exp in the current position, then add to the front
    if new_link.exp > current.exp:      
      new_link.next = self.first
      self.first = new_link

    #Check if exponents are the same
    elif new_link.exp == current.exp:
      self.first.coeff += coeff

    #Check if exp is smaller, go through the list until you find the correct position
    if new_link.exp < current.exp:     
      #As long as you haven't reached the end of both list keep going
      while (current.next != None) and (new_link.exp < current.next.exp):
        current = current.next

      #Check if you reached the end of the list
      if current.next == None:    
        current.next = new_link
      #Check if exponents are the same
      elif current.next.exp == exp:   
        current.next.coeff += coeff
      else:                 
        new_link.next = current.next
        current.next = new_link

  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    #Create a solution Linked List
    solution_list = LinkedList()

    #keep track of where you are in both lists
    current_q    = self.first 
    current_p    = p.first
      
    while (current_q != None) and (current_p != None):  
      #Check if q exponent > p exponent             
      if current_q.exp > current_p.exp:                           
        solution_list.insert_in_order(current_q.coeff, current_q.exp)
        current_q = current_q.next  #Increment through the list

      #Check if q exponent == p exponent
      elif current_q.exp == current_p.exp:                         
        solution_list.insert_in_order((current_q.coeff + current_p.coeff), current_p.exp)
        current_p = current_p.next  #Increment through the list
        current_q = current_q.next   #Increment through the list

      else:                                          
        solution_list.insert_in_order(current_p.coeff, current_p.exp)
        current_p = current_p.next  #Increment through the list

    if current_p != None:                                       
      while current_p != None:
        solution_list.insert_in_order(current_p.coeff, current_p.exp)
        current_p = current_p.next #Increment through the list

    if current_q != None:                                     
      while current_q != None:
        solution_list.insert_in_order(current_q.coeff, current_q.exp)
        current_q = current_q.next #Increment through the list
    return solution_list

  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    #Create a solution Linked List
    solution_list = LinkedList()
    #keep track of where you are p Linked List
    current_p = p.first

    while current_p != None:  
      #keep track of where you are q Linked List                
      current_q = self.first
      while current_q != None:                       
        temp_coeff = current_p.coeff * current_q.coeff      #Multiply coeffs p * q
        temp_exp = current_p.exp + current_q.exp            #Add expo p + q
        solution_list.insert_in_order(temp_coeff, temp_exp) #Insert the correct coeff and exp

        #Increment through the list
        current_q = current_q.next
      current_p = current_p.next

    #Combind like terms aka terms with the same exponents
    index = solution_list.first 
    while index!= None:
      position = index.next
      while position != None and index.exp == position.exp:
        index.coeff = index.coeff + position.coeff          #Add the coeff with the same exponent together
        
        #Increment through the list
        index.next = position.next
        position = position.next
      index = index.next
    return solution_list

  # create a string representation of the polynomial
  def __str__ (self):
    output = ''
    #Keep track of where we are in the list
    current = self.first

    #Check if we reached the end of the list
    while current != None:
      #we do not add coeff if they are 0
      if current.coeff == 0:                   
        current = current.next
        continue
      #add the coeff and exp to the string output to print
      output = output + str(current) + ' + '
      current = current.next
    output = output.rstrip(' + ')
    #return the output
    return output

def main():
  # read data from file poly.in from stdin
  file = sys.stdin

  # create polynomial p
  p = LinkedList()

  #n the number of terms in the first polynomial having non-zero coefficients.
  n = file.readline().strip()                   #number of lines to read
  for i in range(int(n)):
    #read and store in an array
    data_p = file.readline().strip().split() 
    #find the coeff and expo   
    coeff = data_p[0]
    exp = data_p[1]
    p.insert_in_order(int(coeff), int(exp))
  #print(p)

  #reading blank line in between the 2 polynomial
  file.readline()                               

  # create polynomial q
  q = LinkedList()
  #m the number of terms in the second polynomial having non-zero coefficients.
  n = file.readline().strip()
  for i in range(int(n)):
    data_q = file.readline().strip().split()
    #find the coeff and expo
    coeff = data_q[0]
    exp = data_q[1]
    q.insert_in_order(int(coeff), int(exp))
  #print(q)

  # get sum of p and q and print sum
  print(p.add(q))

  # get product of p and q and print product
  print(p.mult(q))

if __name__ == "__main__":
  main()