'''
Complex Number Algebra - Show addition, multiplication, negation, and inversion of complex numbers in separate 
functions. (Subtraction and division operations can be made with pairs of these operations.) Print the results 
for each operation tested.
'''
import re

def complex_to_number(complex_num):
    '''take a complex number of complex number format or string format and return a list of all number portions'''
    
    num_string = str(complex_num)
    
    if 'j' not in num_string:                                     # in the case of only real number
        return [num_string, 0]
    
    elif re.search(r'\d+''[+-]+'r'\d+''j+', num_string) == None:  # in the case of only imaginary number
        return [0, num_string[:-1]]
    
    elif re.search(r'\d+''[+-]+'r'\d+''j+', num_string):          # in the caes of both real and imaginary numbers
        return re.findall('[+-]*'r'\d+', num_string)

def complex_num_addition(num_1, num_2):
    '''addition function'''
    
    list_1 = complex_to_number(num_1)
    list_2 = complex_to_number(num_2)
    
    return complex(int(list_1[0])+int(list_2[0]), int(list_1[1])+int(list_2[1]))

def complex_num_multiplication(num_1, num_2):
    '''multiplication function'''
    
    list_1 = complex_to_number(num_1)
    list_2 = complex_to_number(num_2)
    
    return complex(int(list_1[0])*int(list_2[0])-int(list_1[1])*int(list_2[1]), 
                   int(list_1[0])*int(list_2[1])+int(list_1[1])*int(list_2[0]))

def complex_num_negation(num):
    '''negation function'''
    
    L = complex_to_number(num)
    
    return complex(-int(L[0]), -int(L[1]))

'''Create test class'''
import unittest

class Test_Complex_Number_Operation(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(complex_num_addition(-2j, -1+3j), (-1+1j))
        self.assertEqual(complex_num_addition(-2, -1+3j), (-3+3j))
        self.assertEqual(complex_num_addition(6-2j, -1+3j), (5+1j))
        self.assertEqual(complex_num_addition(8+4j, -1-3j), (7+1j))
        self.assertEqual(complex_num_addition(0, 0), (0j))

    def test_multiplication(self):
        self.assertEqual(complex_num_multiplication(-2j, -1+3j), (6+2j))
        self.assertEqual(complex_num_multiplication(-2, -1+3j), (2-6j))
        self.assertEqual(complex_num_multiplication(6-2j, -1+3j), (20j))
        self.assertEqual(complex_num_multiplication(4j, -1+3j), (-12-4j))
        self.assertEqual(complex_num_multiplication(8+4j, -1-3j), (4-28j))

    def test_negation(self):
        self.assertEqual(complex_num_negation(-2j), (2j))
        self.assertEqual(complex_num_negation(6-2j), (-6+2j))
        self.assertEqual(complex_num_negation(8), (-8))
        self.assertEqual(complex_num_negation(-8+6j), (8-6j))

if __name__ == '__main__':
    unittest.main(verbosity=2)

