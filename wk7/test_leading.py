import leading
import unittest

class leading_substrings(unittest.TestCase):
    '''Tests for leading_substrings.'''

    def test_leading_substrings_list(self):
        '''Test an empty list.'''
        inputted = []
        output = leading.leading_substrings(inputted)
        self.assertIsInstance(output, list, "Returns a list object")


        












if __name__ == "__main__":
	unittest.main()