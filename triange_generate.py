from Triangle import Triangle
import random

def main():
    generate_triangles(25)

# generate n number of triangles and find average, smallest and largest.
def generate_triangles(n_amount):
    average_a = 0
    average_b = 0
    average_c = 0
    valid_triangle = [ 'none' ] * n_amount
    for i in range(n_amount):
        valid_triangle[i] = determine_triangle()
        triangle_class = Triangle(valid_triangle[i][0], valid_triangle[i][1], valid_triangle[i][2])
        average_a = average_a + triangle_class.get_side_a()
        average_b = average_b + triangle_class.get_side_b()
        average_c = average_c + triangle_class.get_side_c()
        print(Triangle(valid_triangle[i][0], valid_triangle[i][1], valid_triangle[i][2]))
    average_a = average_a/n_amount
    average_b = average_b/n_amount
    average_c = average_c/n_amount
    print(average_a, average_b, average_c)
    return valid_triangle

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
