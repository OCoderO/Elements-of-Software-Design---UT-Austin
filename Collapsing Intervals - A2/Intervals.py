#  File: Intervals.py
#  Description: Sorts and merges different intervals
#  Student Name: Nick Lee
#  Student UT EID: bl26395
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 2-1-21
#  Date Last Modified:
import sys
# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval


def merge_tuples(tuples_list):
    # sort the tuples from least to greatest
    for i in range(len(tuples_list)):
        min_index = i
        for j in range(i+1, len(tuples_list)):
            if tuples_list[min_index][0] > tuples_list[j][0]:
                min_index = j
        tuples_list[i], tuples_list[min_index] = tuples_list[min_index], tuples_list[i]


    # merge tuples
    for j in range(len(tuples_list)-1):
        # create a blank list of merged tuples
        new_tuples_list = []
        new_tuple = 0
        # search elements within the array
        for i in range(len(tuples_list)-1):
            # compare the two adjacent elements and merge the tuples
            if tuples_list[i][1] >= tuples_list[i+1][0]:
                if tuples_list[i][1] >= tuples_list[i+1][1]:
                    new_tuple = (tuples_list[i][0], tuples_list[i][1])
                elif tuples_list[i][1] < tuples_list[i+1][1]:
                    new_tuple = (tuples_list[i][0], tuples_list[i+1][1])
                # add the new tuple to the blank list
                new_tuples_list.append(new_tuple)
            elif tuples_list[i][1] < tuples_list[i+1][0]:
                # check if this tuple is higher than the range of the last element in new tuple list
                if new_tuples_list != [] and tuples_list[i][0] > new_tuples_list[-1][1]:
                    new_tuples_list.append(tuples_list[i])
                # if this is the first unmerged tuple in the list, just append
                if new_tuples_list == []:
                    new_tuples_list.append(tuples_list[i])
                # if this is the last unmerged tuple in the list, just append
                if len(tuples_list)-2 == i and tuples_list[i+1][1] > new_tuples_list[-1][1]:
                    new_tuples_list.append(tuples_list[i+1])
        # stop running if there are no more new merged tuples or there is only one element in the list
        if len(new_tuples_list) == len(tuples_list) or len(new_tuples_list) == 0:
            return tuples_list
        else:
            tuples_list = new_tuples_list

    return tuples_list


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval


def sort_by_interval_size(tuples_list):
    # sort interval size
    # copy the list
    tuples_list = tuples_list[:]
    for i in range(len(tuples_list)):
        min_index = i
        for j in range(i+1, len(tuples_list)):
            range1 = tuples_list[min_index][1] - tuples_list[min_index][0]
            range2 = tuples_list[j][1] - tuples_list[j][0]
            if range1 > range2:
                min_index = j
        tuples_list[i], tuples_list[min_index] = tuples_list[min_index], tuples_list[i]
    return tuples_list

# Input: no input
# Output: a string denoting all test cases have passed

'''
def test_cases():
    pass
    assert merge_tuples([(1, 2)]) == [(1, 2)]
    # write your own test cases
    assert sort_by_interval_size([(1,  3), (4, 5)]) == [(4, 5), (1, 3)]
    # write your own test cases
    return "all test cases passed"
'''


def main():
    # open file intervals.in and read the data and create a list of tuples
    n = int(sys.stdin.readline().strip())
    tuples_list = []
    for i in range(n):
        x, y = sys.stdin.readline().split()
        tuples = (int(x), int(y))
        tuples_list.append(tuples)
    # merge the list of tuples
    merged_tuples_list = merge_tuples(tuples_list)
    # sort the list of tuples according to the size of the interval
    sorted_tuples_list = sort_by_interval_size(merge_tuples(tuples_list))
    # run your test cases
    '''
    print (test_cases())
    '''
    # write the output list of tuples from the two functions
    print(merged_tuples_list)
    print(sorted_tuples_list)


if __name__ == "__main__":
    main()
