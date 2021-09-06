#  File: TestLinkedList.py
#  Description:
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 4/7/21
#  Date Last Modified: 4/9/21


class Link (object):
  #links have data and next
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
  
  def __str__(self):
    return str(self.data)

class LinkedList (object):

    # create a linked list
    # you may add other attributes
    def __init__ (self):
        #linked list starts off as an empty list
        self.first = None
        self.last=None


    # get number of links 
    def get_num_links (self):
        count = 0
        current = self.first

        #If current_link == 0 you have reached the end of the linked list 
        while current != None:
            count += 1
            current = current.next
        return count


    # add an item to the beginning of the list
    def insert_first (self, data):
        #Before inserting into the linked list you must create a link
        new_link = Link(data)

        #new_link is pointing to self.first
        new_link.next = self.first
        self.first = new_link

    # add an item to the end of the list
    def insert_last (self, data):
        #Before inserting into the linked list you must create a link
        new_link = Link(data)

        #current keeps track of where we are in the list
        current = self.first

        #if current = None then the list is empty, if empty the first and last link are the same
        if (current == None):
            self.first = new_link
            return

        #The list is not empty so we need to check each link until we get to current = None
        while (current.next != None):
            current = current.next
        current.next = new_link #puts the new link at the very end

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order (self, data): 
        #if the list is empty
        if (self.first == None):
            self.insert_first(data)
            return
        
        #Find out if data to enter should be in the 1st spot
        if data < self.first.data:
            self.insert_first(data)
            return
        
        #Data should be entered after the 1st spot
        else:
            #Before inserting into the linked list you must create a link of the data
            new_link = Link(data)

            #current keeps track of where we are in the list
            current = self.first
            previous = self.first

            while (data > current.data):
                #Check it you have reached the end of the linked list
                if current.next == None:
                    self.insert_last(data)
                    return
                else:
                    previous = current
                    current = current.next
            previous.next = new_link
            new_link.next = current


    # search in an unordered list, return None if not found
    def find_unordered (self, data): 
        #current is a memory location and keeps track of where we are in the list
        current = self.first

        #Check if linked list is empty
        if (current == None):
            return None

        #List is not empty, so check if current location's data != data go to the next location
        while (current.data != data):
            #Check if you have reached the end of the list
            if (current.next == None):
                return None
            else:
                current = current.next
        #You have found the data, return the found memory location
        return current 

    # Search in an ordered list, return None if not found
    def find_ordered (self, data):
      #current is a memory location and keeps track of where we are in the list
      current = self.first

      #Check if linked list is empty
      if current == None:
        return None

      #List is not empty
      else:
        #Search to see if the data is the Linked List 
        while (current.data != data):
          #If you reached the end
          if current.next == None:
            return None
          #Keep searching
          else:
            #Since the Linked list should be ordered once current.next.data > data 
            #We know that the data is not in the list and we can stop
            if current.next.data > data:
              return None 
              #Keep searching
            else:
              current = current.next
        return current
  

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link (self, data):
        #variables to keep track of where we are in the list
        previous = self.first
        current = self.first

        #Check if linked list is empty
        if (current == None):
            return None

        #List is not empty, so check if current location's data != data go to the next location
        while (current.data != data):
            #Check if you have reached the end of the list
            if (current.next == None):
                return None
            #Keep incrementing in the list
            else:
                previous = current
                current = current.next

        #You have found the data to delete
        #If current = the 1st peice of data, just rewrite self.first
        if (current == self.first):
            self.first = self.first.next
        #The data you want to delete is after the 1st peice of data, rewrite over previous.next
        else:
            previous.next = current.next

        #Return the memory location that was deleted
        return current


    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        #variables to keep track of where we are in the list
        current = self.first
        count = 0
        string1 = ''

        #Check if linked list is empty
        if (current == None):
            return ""
        
        #list is not empty, for loop .get_num_links()-1 so no list index out of bounds
        for i in range(self.get_num_links()-1):
            #2 spaces between data
            string1 += str(current.data)
            current = current.next
            count += 1

            #String representation of data 10 items to a line
            if (count) % 10 == 0:
                string1 += '\n'
            else:
                string1 += '  '

        string1 += str(current.data)
        return string1 #Return the string representation of the linked list

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list (self):
      #Create new linked list
      new_list = LinkedList()
      current = self.first

      #Make sure linked list is NOT empty
      while (current != None):
          new_list.insert_last(current.data)
          current = current.next
      return new_list

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list (self): 
      #Create new linked list
      reverse_list = LinkedList()
      current = self.first

      #Make sure linked list is NOT empty
      while (current != None):       
          reverse_list.insert_first(current.data)
          current = current.next
      return reverse_list


    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list (self):
       #Create new linked list 
      sort_Linked = LinkedList()

      #Check if original Linked List is empty
      if self.is_empty():
        return sort_Linked

      current  = self.first
      #Go through the entire list
      for i in range(self.get_num_links()):
        #Insert in the increasing order
        sort_Linked.insert_in_order(current.data)
        current = current.next  
        
      return sort_Linked

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
      #variable to keep track of where we are in the list
      current  = self.first

      #Check if the Linked list is empty or only has 1 value
      if self.is_empty() or self.get_num_links() == 1:
        return True
        
      #Linked List has 2 or more values
      for i in range(self.get_num_links() - 1):
        #Check to see if its in ascending order
        if current.data > current.next.data:
          return False
        current = current.next
        
      return True 

    # Return True if a list is empty or False otherwise
    def is_empty (self): 
      #variables to keep track of where we are in the list
      current = self.first

      #Check if linked list is empty
      if (current == None):
        return True
      return False

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list (self, other): 
      #Keep track of where we are in the list and create a new Linked List
      current = other.first
      merge_Linked = self.copy_list().sort_list()

      #Check if Self Linked List is empty
      if self.is_empty():
        #Check if other Linked List is empty
        if other.is_empty():
          return merge_Linked
        
        #Self Linked List is empty but other is NOT empty
        else:
          merge_Linked = other.copy_list()
          return merge_Linked
        
      #Self is not empty but other Linked List is 
      elif other.is_empty():
        return merge_Linked

      #If both Linked List are not empty
      for i in range(other.get_num_links()):
        #Add data in ascending order
        merge_Linked.insert_in_order(current.data)
        current = current.next
        
      return merge_Linked


    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
      # base case check if both list are empty
      ###should it be data or no?
      # if(self.head.data == other.head.data == None):
      #   return None
      if(self.first.data == None) and (other.first.data == None):
        return True
      # base case check if one of the list is empty
      # elif (other.first.data == None) or (self.first.data == None):
      #   return False
      #loop for checking to see if two lists are the same
      # selfhead=self.first
      # otherhead=other.first
      for i in range(self.get_num_links()):
          if(self.first.data != other.first.data):
              return False
          #if theyre not the same 
          #then redefine the first of both lists
          else: 
            self.first = self.first.next
            other.first = other.first.next
      return True



    # do not change the original list
    def remove_duplicates (self):  #Wendy
        finallist = []
        remove_duplicateslist = LinkedList()
        current = self.first
        while (current != None):
          # check if value exists
          while (current.data not in finallist):
            # and removing all duplicates. Do not change the order of the elements.
            finallist.append(current.data)
            remove_duplicateslist.insert_last(current.data)			
            self.first = self.first.next
            # Return a new list that has only the first occurence of an elemen
          #update the next item in list
          current = current.next
        return remove_duplicateslist

def main():
    testList = LinkedList()

    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    testList.insert_first(1)
    testList.insert_first(2)
    testList.insert_first(3)
    testList.insert_first(4)
    testList.insert_first(5)
    testList.insert_first(6)
    testList.insert_first(7)
    testList.insert_first(8)
    testList.insert_first(9)
    testList.insert_first(10)
    testList.insert_first(11)
    testList.insert_first(12)
    print(testList)


    # Test method insert_last()
    # testList.insert_last(1)
    # testList.insert_last(2)
    # testList.insert_last(3)
    # testList.insert_last(4)
    # testList.insert_last(5)
    # testList.insert_last(6)
    # testList.insert_last(7)
    # testList.insert_last(8)
    # testList.insert_last(9)
    # testList.insert_last(10)
    # testList.insert_last(11)
    # testList.insert_last(12)
    #print(testList)

    # Test method insert_in_order()
    # testList.insert_in_order(3)
    # testList.insert_in_order(1)
    # testList.insert_in_order(10)
    # testList.insert_in_order(2)
    # testList.insert_in_order(4)
    # testList.insert_in_order(5)
    # testList.insert_in_order(9)
    # testList.insert_in_order(6)
    # testList.insert_in_order(7)
    # testList.insert_in_order(8)
    # testList.insert_in_order(11)
    # testList.insert_in_order(12)
    # print(testList)

    # Test method get_num_links()
    #print(testList.get_num_links())


    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there 
    # testList.insert_in_order(3)
    # testList.insert_in_order(1)
    # testList.insert_in_order(10)
    # testList.insert_in_order(2)
    # testList.insert_in_order(4)
    # testList.insert_in_order(5)
    # testList.insert_in_order(9)
    # testList.insert_in_order(6)
    # testList.insert_in_order(7)
    # testList.insert_in_order(8)
    # testList.insert_in_order(11)
    # testList.insert_in_order(12)
    # print(testList.find_unordered(3)) #data is there
    # print(testList.find_unordered(13))#data is not there 

    # Test method find_ordered() 
    # # Consider two cases - data is there, data is not there 
    # testList.insert_in_order(3)
    # testList.insert_in_order(1)
    # testList.insert_in_order(10)
    # testList.insert_in_order(2)
    # testList.insert_in_order(4)
    # testList.insert_in_order(5)
    # testList.insert_in_order(9)
    # testList.insert_in_order(6)
    # testList.insert_in_order(7)
    # testList.insert_in_order(8)
    # testList.insert_in_order(11)
    # testList.insert_in_order(12)
    # print(testList.find_unordered(4)) #data is there
    # print(testList.find_unordered(13))#data is not there 

    # Test method delete_link()
    # Consider two cases - data is there, data is not there 

    # Test method copy_list()

    # Test method reverse_list()

    # Test method sort_list()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted

    # Test method is_empty()

    # Test method merge_list()

    # Test method is_equal()
    # # Consider two cases - lists are equal, lists are not equal
    # testList2=LinkedList()
    # testList2.insert_first(3)
    # testList.insert_first(13)
    # print("Testing is_equal().")
    # print(testList.is_equal (testList2))

    # # Test remove_duplicates()
    # #     Consider two cases - data is there, data is not there 
    # testList.insert_first(3)
    # testList.insert_first(13)
    # testList.insert_first(3)
    # testList.insert_first(3)
    # print(testList.remove_duplicates()) 
    ##data is there
    # print(testList.remove_duplicates())
    #data is not there 


if __name__ == "__main__":
    main()
