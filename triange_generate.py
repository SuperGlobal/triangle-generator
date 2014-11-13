# CPT 101 Programming in Python Fall 2014
# Name: Mike Morabito
# Date: 11/12/2014
# Description: Utilizes my triangle class, creates triangles to specs.
#              Pickles and unpickles the list of triangles.
#

from Triangle import Triangle
import random
import pickle

def main():
    triangle_dictionary = { }
    triangle_list = generate_triangles(25, triangle_dictionary)
    triangle_add = add_triangles(75)
    pickle_time(triangle_list)
    unpickled_list = unpickle_time()
    triangle_list.extend(triangle_add)

# serialization of the list of circle objects
def pickle_time(cc):
    output_file = open('triangle_objects.dat', 'wb')
    pickle.dump(cc, output_file)
    output_file.close()

# unpickle a file
def unpickle_time():
    pickled_file = open('triangle_objects.dat', 'rb')
    load_pickled = pickle.load(pickled_file)
    pickled_file.close()
    return load_pickled

# generate n number of triangles and find average, smallest and largest.
def add_triangles(n_amount):
    valid_triangle = [ 'none' ] * n_amount
    for i in range(n_amount):
        valid_triangle[i] = determine_triangle()
    return valid_triangle

# generate n number of triangles and find average, smallest and largest.
def generate_triangles(n_amount, dictionary):
    average_a = 0
    average_b = 0
    average_c = 0
    smallest_triangle = 0
    largest_triangle = 0
    valid_triangle = [ 'none' ] * n_amount
    valid_areas = [ 'none' ] * n_amount
    for i in range(n_amount):
        valid_triangle[i] = determine_triangle()
        triangle_class = Triangle(valid_triangle[i][0], valid_triangle[i][1], valid_triangle[i][2])
        valid_areas[i] = triangle_class.get_area()
        average_a = average_a + triangle_class.get_side_a()
        average_b = average_b + triangle_class.get_side_b()
        average_c = average_c + triangle_class.get_side_c()
    # calculating the average point individually
    average_a = average_a/n_amount
    average_b = average_b/n_amount
    average_c = average_c/n_amount
    average_triangle = [average_a, average_b, average_c]
    valid_areas.sort()
    dictionary['Average: '] = average_triangle
    dictionary['Largest: '] = valid_areas[n_amount-1]
    dictionary['Smallest: '] = valid_areas[0]
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
