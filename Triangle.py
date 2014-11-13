import math

class Triangle:

    # get and set the sides to private vars
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    # get the perimeter of the triangle
    def get_perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

    # get the area of the triangle
    def get_area(self):
        s_var = (self.__side_a + self.__side_b + self.__side_c)/2
        return math.sqrt(s_var(s_var - self.__side_a)(s_var - self.__side_b)(s_var - self.__side_c))

    # get side a
    def get_side_a(self):
        return self.__side_a

    # get side b
    def get_side_b(self):
        return self.__side_b

    # get side c
    def get_side_c(self):
        return self.__side_c

    # print out the points
    def __str__(self):
        return 'A = ' + str(self.__side_a) + ' B = ' + str(self.__side_b) + ' C = ' + str(self.__side_c)
