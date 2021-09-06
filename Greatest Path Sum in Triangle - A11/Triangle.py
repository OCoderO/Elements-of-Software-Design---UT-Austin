#  File: Triangle.py
#  Description:
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created:3/25/2021
#  Date Last Modified: 3/29/2021

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
#(wendy)

def brute_force (grid):
  #every possible path stored into one list
  Sum_Stored = []
  #use helper function
  findmax(grid,0,0,0,Sum_Stored) #recursive call
  return max(Sum_Stored)

#brute_force helper
def findmax(grid, horz, vert, findxmax_sum, Sum_Stored):
  #if the row is the length of the triangle
  #add it to sum list
  if(horz == len(grid)):
    Sum_Stored.append(findxmax_sum)
  #if not just return the max of the upcoming lines 
  ###is this correct????     
  else:
    return (findmax(grid, horz+1, vert, findxmax_sum + grid[horz][vert], Sum_Stored) , findmax(grid, horz+1, vert+1, findxmax_sum + grid[horz][vert],Sum_Stored))
    print(grid[horz][vert])


# returns the greatest path sum using greedy approach
def greedy (grid): # O(N) notation
  sum =  grid[0][0]
  col = 0
  for idx in range(1,len(grid)):
    #Check if the left number is the larger than the number on the right
    if grid[idx][col] > grid[idx][col+1]:
      sum += grid[idx][col]
    else:
      #The right number is larger than the number on the left
      sum += grid[idx][col+1]
      col = col + 1 #Change col so that way the you keep track of which column your in to look at the indexs on the row below
  return sum


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  return max(dc_helper(grid, 0, 0, 0))

def dc_helper (grid, i, j, sum):
  # Check if we have reached the bottom of the triangle
  if i >= len(grid):
    return [sum]
  else:
    #You will recursively search all paths, but in each recursive call only returns a single value.
    if i == len(grid) - 1:
      # Instead of keeping track of all the possible sums, you only obtain the maximum one.
      return dc_helper(grid, i + 1, j, sum + grid[i][j])
    else:
      return dc_helper(grid, i + 1, j, sum + grid[i][j]) + dc_helper(grid, i + 1, j + 1, sum + grid[i][j])

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):# O(N^2)
  #This function is a memorized version of divide_conquer(). 
  return dyn_helper (grid, 0, 0)

def dyn_helper (grid, row, col):
  # Check if we have reached the bottom of the triangle
  if row >= len(grid):
    return 0
  else:
    # You can have another list to store the maximum paths in each cell, and moving from the bottom of the triangle to the top.
    a = grid[row][col] + dyn_helper (grid, row + 1, col)
    b = grid[row][col] + dyn_helper (grid, row + 1, col + 1)
    if a > b:
      return a
    else:
      return b
      
# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()
