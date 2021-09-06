#  File: Hull.py
#  Description: Creating convex hull around the given points
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 2/21/2021
#  Date Last Modified: 3/1/2021

import sys
import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
#def det (p, q, r):

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  #Create an empty list upper_hull that will store first two points p_1 and p_2 in order into the upper_hull.
  upper_hull = [sorted_points[0],sorted_points[1]]

  for i in range(2,len(sorted_points)):
    upper_hull.append(sorted_points[i])
    while len(upper_hull) >= 3:
      #Call determinate method to find out which way it turns
      turn = det(upper_hull[-3],upper_hull[-2],upper_hull[-1])

      if turn < 0:    #Right turn, so continue
        break
      elif turn > 0:  #Left turn, so delete the middle point
        upper_hull.pop(-2)
      else:           #Collinear, so delete the middle point
        upper_hull.pop(-2)

  #Create an empty list lower_hull that will store last two points p_n and p_n-1 in order into the upper_hull.
  lower_hull = [sorted_points[-1],sorted_points[-2]]

  #for i in range(starting index, ending index, incremetation)
  for i in range(len(sorted_points)-3, -1, -1):
    lower_hull.append(sorted_points[i])

    while len(lower_hull) >= 3:
     #Call determinate method to find out which way it turns
      turn = det(lower_hull[-3],lower_hull[-2],lower_hull[-1])

      if turn < 0:    #Right turn, so continue
        break
      elif turn > 0:  #Left turn, so delete the middle point
        lower_hull.pop(-2)
      else:           #Collinear, so delete the middle point
        lower_hull.pop(-2)

  #Remove the first and last points for lower_hull to avoid duplication
  lower_hull.pop(0)
  lower_hull.pop(-1)

  #Append the points in the upper_hull with the points in the lower_hull
  convex_hull = upper_hull + lower_hull
  return convex_hull


# Input: 3 Point objects
# Output: which way they turn
def det(p, q, r):
  det = (p.x * q.y) + (q.x * r.y) + (r.x * p.y) - (p.y * q.x) - (q.y * r.x) - (r.y * p.x)
  return det


# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  det = 0
  for i in range(len(convex_poly)-1):
    det += (convex_poly[i].x * convex_poly[i+1].y) - (convex_poly[i].y * convex_poly[i+1].x)
  det += (convex_poly[len(convex_poly)-1].x * convex_poly[0].y) - (convex_poly[len(convex_poly)-1].y * convex_poly[0].x)
  area = (1/2) * abs(det)
  return area

  

# Input: no input
# Output: a string denoting all test cases have passed
#def test_cases():
  # write your own test cases
 

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  num_points = int(sys.stdin.readline().strip()) 

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline().strip().split()
    x = int (line[0])
    y = int (line[1])
    points_list.append(Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  # get the convex hull
  convex_hull_list = convex_hull(sorted_points)

  # run your test cases
  # print your results to standard output

  # print the convex hull
  print("Convex Hull")
  for i in range(len(convex_hull_list)):
    print(convex_hull_list[i].__str__())

  # get the area of the convex hull
  area = area_poly(convex_hull_list)

  # print the area of the convex hull
  print("\nArea of Convex Hull =", area)

if __name__ == "__main__":
  main()