#  File: Josephus.py
#  Description:
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 4/10/21
#  Date Last Modified: 4/12/21

import sys

class Link(object):
  #links have data and next
  def __init__ (self, data, next = None):
    self.data = data #data element of link
    self.next = next  #actual link element
  

class CircularList(object):
    # Constructor
    def __init__ ( self ):
       #Create object of data not link. Links will be made in insert function 
        self.first = None 

    # Insert an element (value) in the list
    def insert ( self, data ):
      #Creates a new link to be inserted at the end of list 
      new_link = Link (data, self.first)
      #Using self.first as next address to make it circular
      current = self.first

      #Check if the list is empty
      if (current == None):
        #Create a new link 
        self.first = new_link 
        self.first.next = self.first
        return 
  
      #For a non-empty list, reaches last link in list
      while (current.next != self.first):
        current = current.next
      # After reaching last link, assigns next of last link to the new_link
      current.next = new_link 




    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find ( self, data ):
      #check if the list is empty
      if self.first == None:
        return None
      #assign the traversal starting point as the first link
      current = self.first
      #traverse the list until key is found, return none if not found
      while (current.data != data):
        if current.next == self.first:
          return None
        else:
          current = current.next

      #return current link if found
      return current
            


    def delete(self, data):
        #Variables to keep track of where we are in the list
        current = self.first
        previous = self.first

        # check if the list is empty
        if self.first == None:
            return None
        #Check if the list is only 1 element long and thats the element deleted
        if self.first == self.first.next:
            self.first = None
            return current
        
        #Go through the list as long as you dont reach the end
        while previous.next != self.first:
            previous = previous.next

        #Check if you have reached the end of the list
        if current == None:
            return None

        else:
            #Go through the list
            if current.next == self.first and current.data == data:
                return current
        #Go through the list
        while (current.data != data):
            if current.next == self.first:
                return None
            else:
                #Increment variables
                previous = current
                current = current.next
        if current == self.first:
            self.first = self.first.next
        previous.next = current.next
        return current
        
    # Delete the nth Link starting from the Link start 
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after ( self, start, n ):
      current = self.find(start) # starts from start
      # n -1 because current is also counted
      for count in range (0, n-1):
        current = current.next
      dead = self.delete(current.data)
      # Returns the new start, no longer contains dead
      return (dead, current.next.data)




    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__ 
    # format for normal Python lists
    def __str__ ( self ):
      #if the list is empty, return none
      if self.first == None:
        return "[]"
      
      
      #List is not empty
      else:
        #format the list as a normal looking python list
        output = "["
        current = self.first
        #Go through the list until you reach the end
        while current.next != self.first:
          output += str(current.data) + ", "
          current = current.next
        output += str(current.data) + "]"
        return output
                
    
      
def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)
    
    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)

    #Create Circular List
    soldiers_list = CircularList()
    
    #Populate the list with the number of soldiers
    for i in range(1, num_soldiers+1):
      soldiers_list.insert(i)
    
    # #Call delete_after
    for j in range (1, num_soldiers + 1): 
      dead, start_count = soldiers_list.delete_after(start_count, elim_num) 
      print(str(dead.data))


if __name__ == "__main__":
  main()

