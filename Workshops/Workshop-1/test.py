# Paul Kreischer - pck0010@auburn.edu
# SQA - Workshop 1

import unittest
import source  # type: ignore

# odd numbered tests pass, even numbered tests fail
class TestCalc(unittest.TestCase):
    def testSub1(self):
        self.assertEqual(1, source.performSub(3, 2), "Error in subtraction function")

    def testSub2(self):
        self.assertEqual(5, source.performSub(6, 2), "Error in subtraction function")
        
    def testAdd1(self):
        self.assertEqual(4, source.performAdd(1, 3), "Error in addition function")
        
    def testAdd2(self):
        self.assertEqual(9, source.performAdd(5, 3), "Error in addition function")
        
    def testMul1(self):
        self.assertEqual(6, source.performMul(2, 3), "Error in multiplication function")

    def testMul2(self):
        self.assertEqual(16, source.performMul(5, 3), "Error in multiplication function")

    def testDiv1(self):
        self.assertEqual(2, source.performDiv(6, 3), "Error in division function")

    def testDiv2(self):
        self.assertEqual(1, source.performDiv(5, 0), "Error in division function")
    
    def testSqrt1(self):
        self.assertEqual(4, source.performSqrt(16), "Error in square root function")

    def testSqrt2(self):
        self.assertEqual(1, source.performSqrt(-9), "Error in square root function")
   
if __name__ == '__main__': 
    unittest.main()
