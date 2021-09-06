#  File: Cipher.py
#  Description: Ciphers through creating matrix
#  Student Name: Nick Lee
#  Student UT EID: bl26395
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 2-6-21
#  Date Last Modified: 2-8-21

import sys
# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string


def encrypt ( strng ):
    # find the smallest square size M
    for i in range(10):
        if len(strng) <=i ** 2:
            M = i
            break

    # create a list from a string
    lst_in = []
    for i in range(len(strng)):
        if len(lst_in) < M:
            sub_lst = []
            for j in range(M):
                try:
                    sub_lst.append(strng[(i * M) + j])
                except IndexError:
                    sub_lst.append('*')
            lst_in.append(sub_lst)
    # encrypt
    for x in range(M):
        for y in range(x):
            rotated_list = lst_in[x][y]
            lst_in[x][y] = lst_in[y][x]
            lst_in[y][x] = rotated_list
    for x in range(M):
        for y in range(M // 2):
            switched_list = lst_in[x][y]
            lst_in[x][y] = lst_in[x][M - y - 1]
            lst_in[x][M - y - 1] = switched_list
    # print new encrypted string
    new_str = ''
    for x in range(M):
        for y in range(M):
            if lst_in[x][y] != '*':
                new_str += lst_in[x][y]
    return new_str

# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string


def decrypt ( strng ):
    # find the smallest square size M
    for i in range(10):
        if len(strng) <= i ** 2:
            M = i
            break

    # create an empty list
    lst_in = []
    for i in range(len(strng)):
        if len(lst_in) < M:
            sub_lst = []
            for j in range(M):
                try:
                    sub_lst.append(strng[(i * M) + j])
                except IndexError:
                    sub_lst.append('*')
            lst_in.append(sub_lst)
    # decrypt
    for x in range(M - 1, -1, -1):
        for y in range(x - 1, -1, -1):
            rotated_list = lst_in[x][y]
            lst_in[x][y] = lst_in[y][x]
            lst_in[y][x] = rotated_list
    for x in range(M // 2):
        lst_in[x], lst_in[M - x - 1] = lst_in[M - x - 1], lst_in[x]
    # print the string
    new_str = ''
    for x in range(M):
        for y in range(M):
            if lst_in[x][y] != '*':
                new_str += lst_in[x][y]
    return new_str

def main():
    # read the two strings P and Q from standard input
    P = str(sys.stdin.readline().strip())
    Q = str(sys.stdin.readline().strip())
    # encrypt the string P
    P = encrypt(P)
    # decrypt the string Q
    Q = decrypt(Q)
    # print the encrypted string of P and the decrypted string of Q to standard out
    print(P)
    print(Q)
if __name__ == "__main__":
    main()