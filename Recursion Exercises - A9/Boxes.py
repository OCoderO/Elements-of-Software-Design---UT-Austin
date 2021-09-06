#  File: Boxes.py
#  Description:
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created:3/23/2021
#  Date Last Modified: 3/25/2021

import sys


# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes(box_list, sub_set, idx, all_box_subsets):
    #Modified code from the subsets code we went over in class
    if (idx == len(box_list)): #Check it you have reached the end of the list
        all_box_subsets.append(sub_set)
    else:
        temp = sub_set[:] #Temporaty variable
        sub_set.append(box_list[idx]) #
        sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
        sub_sets_boxes(box_list, temp, idx + 1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets(all_nesting_boxes):
    #Below are 3 different types of counting variables
    largest_size = 0
    instances_of_largest_size = 0
    count = 1

    #Use nested for loops because all_nesting_boxes is a 3D list
    for subset in range(len(all_nesting_boxes)):
        for box in range(len(all_nesting_boxes[subset]) - 1):
            #First determine whether the subset is nesting (does_fit() 
            if does_fit(all_nesting_boxes[subset][box],
                        all_nesting_boxes[subset][box + 1]):
                count += 1 #Counts up the number of boxes in the subset that fit

            #Checks that all the boxes in the subsets fit into one another
            if count == len(all_nesting_boxes[subset]):
              if largest_size < len(all_nesting_boxes[subset]): #Checks that largest size will only increase
                largest_size = len(all_nesting_boxes[subset])

                instances_of_largest_size = 0 #Clears instances_of_largest_size 
              
              if largest_size == len(all_nesting_boxes[subset]): #Check to see how many instances of subsets with the number of nesting boxes
                instances_of_largest_size += 1

        count = 1 #Clears count 
    
    return largest_size,instances_of_largest_size
    


# returns True if box1 fits inside box2
def does_fit(box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


def main():
    # read the number of boxes
    num_boxes = int(sys.stdin.readline().strip())
    #print(num_boxes)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range(num_boxes):
        box = sys.stdin.readline().strip().split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)

    # print to make sure that the input was read in correctly
    #print (box_list)
    #print()

    # sort the box list
    box_list.sort()

    # print the box_list to see if it has been sorted.
    # print(box_list)
    # print()

    # create an empty list to hold all subset of boxes
    all_box_subsets = []

    # create a list to hold a single subset of boxes
    sub_set = []

    # generate all subsets of boxes and store them in all_box_subsets
    sub_sets_boxes(box_list, sub_set, 0, all_box_subsets)

    # all_box_subsets should have a length of 2^n where n is the number
    # of boxes

    # go through all the subset of boxes and only store the
    # largest subsets that nest in all_nesting_boxes
    #all_nesting_boxes is a tuple that contains: largest number of boxes that fit & the number of sets of such boxes
    all_nesting_boxes = largest_nesting_subsets(all_box_subsets)

    # print the largest number of boxes that fit
    print(all_nesting_boxes[0])
    
    # print the number of sets of such boxes
    print(all_nesting_boxes[1])
    


if __name__ == "__main__":
    main()
