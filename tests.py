import unittest
from flatonacci import flatonacci

# values = flatonacci([1,1,2.2], 8)
# print(values, len(values))

class TestFlatonacci(unittest.TestCase):

    def setUp(self):
        self.signature_valid = [1,1,1]
        self.signature_with_string = [1,2,'s']
        self.signature_bigger = [1,2,3,4]
        self.signature_smaller = [1,2]
        self.n_valid_small = 1
        self.n_valid_big = 5 
        self.n_string = 's'
        self.n_negative = -2
        self.n_zero = 0

    def test_n_values(self):
        print('Test for n values: n is not number, n is negative, n is zero')
        signature_valid = [1,2,3]
        n_string = 's'
        n_negative = -2
        self.assertRaises(ValueError, flatonacci, signature_valid, n_string)
        self.assertRaises(ValueError, flatonacci, signature_valid, n_negative)
        self.assertEqual(flatonacci(signature_valid, 0),[])

    def test_signature_values(self):
        print('Test for signature values: size and not number values')
        signature_with_string = [1,2,'s']
        signature_smaller = [1,2]
        signature_bigger = [1,2,3,4,5]
        n = 5
        self.assertRaises(ValueError, flatonacci, signature_with_string, n)
        self.assertRaises(ValueError, flatonacci, signature_smaller, n)
        self.assertRaises(ValueError, flatonacci, signature_bigger, n)

    def test_sequence_results(self):
        print('Test for sequence values: sequence size and results validation')
        signature_example = [1,1,1]
        sequence_small = [1,1,1,3,5]
        sequence_big = [1,1,1,3,5,9,17,31]
        n_small = 2
        n_big = 8
        self.assertEqual(len(flatonacci(signature_example, n_small)), n_small + len(signature_example))
        self.assertEqual(len(flatonacci(signature_example, n_big)), n_big)
        self.assertEqual(flatonacci(signature_example, n_small), sequence_small)
        self.assertEqual(flatonacci(signature_example, n_big), sequence_big)
        
        