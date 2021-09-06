#  File: Spiral.py
#  Description: Creates a table of numbers that counts in a spiral
#  Student Name: Nick Lee
#  Student UT EID: bl26395
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 1-27-21
#  Date Last Modified: 1-29-21

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
import sys

def create_spiral ( n ):
    # Create blank matrix
    rows, cols = (n,n)
    spiral = [[0 for i in range(cols)] for j in range(rows)]

    # Find the middle
    row_idx = n // 2
    col_idx = n // 2
    count = 1

    spiral[row_idx][col_idx] = count
    
    for i in range(1,n):
        # When N square is odd
        if i % 2 == 1:
            count += 1

            # right 1
            col_idx += 1
            spiral[row_idx][col_idx] = count

            # down n
            for j in range(i):
                count += 1
                row_idx += 1
                spiral[row_idx][col_idx] = count

            # left n
            for k in range(i):
                count += 1
                col_idx -= 1
                spiral[row_idx][col_idx] = count

        # When N square is even
        if i % 2 == 0:
            count += 1

            # left 1
            col_idx -= 1
            spiral[row_idx][col_idx] = count

            # up n
            for j in range(i):
                count += 1
                row_idx -= 1
                spiral[row_idx][col_idx] = count

            # right n
            for k in range(i):
                count += 1
                col_idx += 1
                spiral[row_idx][col_idx] = count
    return spiral

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
    x = 0
    y = 0

    # find x, y in spiral
    for i in range(len(spiral)):
        for j in range(len(spiral)):
            if spiral[i][j] == n:
                x = i
                y = j

    # Input: The x-y coord of the input number
    # Output: The surrounding number that is
    #         around the input number
    def up(x, y):
        if x - 1 < 0:
            return 0
        return spiral[x - 1][y]
    def right(x, y):
        if y + 1 >= len(spiral):
            return 0
        return spiral[x][y + 1]
    def down(x, y):
        if x + 1 >= len(spiral):
            return 0
        return spiral[x + 1][y]
    def left(x, y):
        if y - 1 < 0:
            return 0
        return spiral[x][y - 1]
    def up_right(x,y):
        if x - 1 < 0 or y + 1 > len(spiral)-1:
            return 0
        return spiral[x-1][y+1]
    def down_right(x,y):
        if x + 1 >= len(spiral)-1 or y + 1 > len(spiral)-1:
            return 0
        return spiral[x+1][y+1]
    def down_left(x,y):
        if x + 1 > len(spiral)-1 or y - 1 < 0:
            return 0
        return spiral[x+1][y-1]
    def up_left(x,y):
        if x - 1 < 0 or y - 1 < 0:
            return 0
        return spiral[x-1][y-1]

    # Return 0 if the numbers are out of bounds
    if n > len(spiral) ** 2:
        return 0
    else:
        moves = [
            up(x,y), up_right(x,y), right(x,y), down_right(x,y),
            down(x,y), down_left(x,y), left(x,y), up_left(x,y)]
        return sum(moves)

def main():
    # read the input file
    n = int(sys.stdin.readline().strip())

    # create the spiral
    spiral = create_spiral(n)

    # add the adjacent
    for line in sys.stdin:
        num = int(line)
        # print the result
        print(sum_adjacent_numbers(spiral, num))

if __name__ == "__main__":
    main()
