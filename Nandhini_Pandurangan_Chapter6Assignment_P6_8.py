# CIS40: Summer2020: Chapter 6 Assignment: Nandhini Pandurangan
# This program computes the alternating sum from a set of integers provided by the user


def read_input():
    """ Gathers input and performs input validation with exception handling"""

    flag = True

    while flag:
        try:
            num_list = input("Please enter any amount of integers separated by a space: ").split()

            # converting the contents of the list into integers
            for i in range(len(num_list)):
                num_list[i] = int(num_list[i])

            flag = False

        except ValueError:
            print("\n ERROR! Please enter valid integers separated by a space\n ")

    return num_list


def compute_alternating_sum(num_list):
    """ Computes the alternating sum """

    alt_sum = 0

    # even indexed elements are added and odd indexed elements are subtracted
    for i in range(len(num_list)):
        if i % 2 == 0:
            alt_sum += num_list[i]
        else:
            alt_sum -= num_list[i]

    return alt_sum



def print_alternating_sum(num_list, alt_sum):
    """ Outputs the alternating sum """

    # *num_list unpacks the list to only give the values
    print("\nThe alternating sum of", *num_list, "is", alt_sum)


def main():
    """ Calls appropriate functions to compute alternating sum """

    num_list = read_input()
    alternating_sum = compute_alternating_sum(num_list)
    print_alternating_sum(num_list, alternating_sum)


# calling main
main()

""" 
Output1: 

Please enter any amount of integers separated by a space: 1 4 9 16 9 7 4 9 11

The alternating sum of 1 4 9 16 9 7 4 9 11 is -2
------------------------------------------------------------------------------
Output2: 

Please enter any amount of integers separated by a space: 1 2 3 hello 4 5 6

 ERROR! Please enter valid integers separated by a space
 
Please enter any amount of integers separated by a space: h e l l o

 ERROR! Please enter valid integers separated by a space
 
Please enter any amount of integers separated by a space: 1 2 3 4 -9

The alternating sum of 1 2 3 4 -9 is -11
"""