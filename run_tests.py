import unittest
from tests.book_test import TestBook

if __name__ == '__main__':
     unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestBook))
    
