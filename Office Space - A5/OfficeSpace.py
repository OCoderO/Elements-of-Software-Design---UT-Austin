#  File: OfficeSpace.py
#  Description: Dividing up office space
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 2/12/2021
#  Date Last Modified: 2/15/2021

import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
  length = int(rect[2]) - int(rect[0])
  width = int(rect[3]) - int(rect[1])
  area = length * width
  return area


# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
  #Check if rectangles intersect
  check = intersect(rect1,rect2)

  if check == True:
    overlap_x = abs(max(rect1[0], rect2[0]) - min(rect1[2], rect2[2]))
    overlap_y = abs(max(rect1[1], rect2[1]) - min(rect1[3], rect2[3]))
    overlap_leftx = (min(max(rect1[0], rect2[0]), min(rect1[2], rect2[2])))
    overlap_lefty = (min(max(rect1[1], rect2[1]), min(rect1[3], rect2[3])))
    overlap_rightx=(max(max(rect1[0], rect2[0]), min(rect1[2], rect2[2])))
    overlap_righty=(max(max(rect1[1], rect2[1]),min(rect1[3], rect2[3])))
    if (overlap_x >= 0) and (overlap_y >= 0): ####does the <= matters??
      return (overlap_leftx,overlap_lefty,overlap_rightx,overlap_righty)
    #print(overlap_leftx,overlap_lefty,overlap_rightx,overlap_righty)
  return (0,0,0,0)

#Helper function to check for intersection
def intersect(rect1, rect2):
   #Check to see if two rectangles intersect
   if (rect1[0] > rect2[3]) or (rect2[0] > rect1[3]):
     if (rect1[1] <= rect2[3]) or (rect2[1] < rect1[3]):
       return False
   return True

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
  #Dimensions of the 2D list
  width = len(bldg[0]) #33
  height = len(bldg)   #2

  #Employee's 4 integers for their cubicle
  x1 = int(rect[0])
  y1 = int(rect[1])
  x2 = int(rect[2])
  y2 = int(rect[3])
  count = 0   #Keeps track of uncontested space

  #print out building 2D list
  # for row in bldg:
  #   print(*row)

  #Go through the 2D list counting the uncontested space
  for row in range(height):
    for col in range(width):
      if row >= (height - y2) and row < (height - y1):  #Iterating over the row manipulate the y value
          if col >= x1 and col < x2:                    #Iterating over the column manipulate the x value                   
            if bldg[row][col] == 1:                     #Check to see if it is unallocated
              count += 1
  return count
    

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
  #create an 2D list with the dimensions from office tuple
  width = int(office[2]) #33
  height = int(office[3]) #26
  office_list = [[0 for x in range(width)] for y in range(height)] 

  #4 integers in for each employee's cubicle
  for index in range(len(cubicles)):
    x1 = int(cubicles[index][0])
    y1 = int(cubicles[index][1])
    x2 = int(cubicles[index][2])
    y2 = int(cubicles[index][3])

    #Change the 2D list to reflect where each employee's cubicle is
    for row in range(height):
      for col in range(width):
        if row >= (height - y2) and row < (height - y1):  #Iterating over the row manipulate the y value
          if col >= x1 and col < x2:                      #Iterating over the column manipulate the x value                    
            if office_list[row][col] == 0:                #Check to see if it is unallocated
              office_list[row][col] = 1
            else: #contested space; count how many people want that index
              office_list[row][col] = office_list[row][col] + 1

  #print out building 2D list
  # for row in office_list:
  #   print(*row)
  return office_list

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
  count = 0
  for row in range(len(bldg)):
    for col in range(len(bldg[0])):
      if bldg[row][col] == 0:
        count += 1
  return count

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
  count = 0
  for row in range(len(bldg)):
    for col in range(len(bldg[0])):
      if bldg[row][col] > 1:
        count += 1
  return count

# Input: no input
# Output: a string denoting all test cases have passed
#def test_cases ():
  #assert area ((0, 0, 1, 1)) == 1
  # write your own test cases
  #return "all test cases passed"



def main():
  # read the data
  w,h = sys.stdin.readline().strip().split(" ")
  num_employees = int(sys.stdin.readline().strip())

  #Create a list to hold employee's name and 4 integers for each employee
  employee_list = []
  for line in sys.stdin.readlines():
    employee_list.append(line.strip().split(" "))

  #Create a list of tuples for containing each of the employee's 4 integers 
  cubicle_list = []
  for employee in range(num_employees):
    cubicle_list.append(tuple(employee_list[employee][1:5]))

  #Tuple of total office space
  office_tuple = (0,0,w,h)

  # run your test cases
  # print the following results after computation


  # compute the total office space 
  print("Total", area(office_tuple))

  #Call request_space Method
  bldg = request_space(office_tuple,cubicle_list)

  # compute the total unallocated space
  print("Unallocated",unallocated_space(bldg))

  # compute the total contested space
  print("Contested", contested_space(bldg))

  # compute the uncontested space that each employee gets
  for i in range(num_employees):
    print(employee_list[i][0],uncontested_space(bldg,cubicle_list[i]))
    

if __name__ == "__main__":
  main()