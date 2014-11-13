from Triangle import Triangle
import random

def main():
    valid_triangle = determine_triangle()
    print(Triangle(valid_triangle[0], valid_triangle[1], valid_triangle[2]))

# generates a list of random numbers
def generate_list():
    random_num = [ 0, 0, 0 ]
    for i in range(0,3):
        random_num[i] = random.randint(1,20)
    return random_num

# sorts the list and determines if the numbers can be a  possible triangle
def determine_triangle():
    triangle_flag = False
    while triangle_flag != True:
        my_list = generate_list()
        my_list.sort()
        smallest_side = my_list[0]
        middle_side = my_list[1]
        largest_side = my_list[2]
        sum_of_legs = smallest_side + middle_side
        if sum_of_legs > largest_side:
            triangle_flag = True
    return my_list

main()
