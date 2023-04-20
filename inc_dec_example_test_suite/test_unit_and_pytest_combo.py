import unittest
import inc_dec  

def test_single_pytest():
    assert inc_dec.increment(-1) == 2
	
class test_class_unittest_combo_file(unittest.TestCase):
    #This test class is not recognized by the discovery function and that is in line with what currently happens on our repo.

    def test_combo1_function_unittest(self):
        self.assertEqual(inc_dec.increment(5), 6, "Should be 6")

    def combo2_function_unittest(self):
        self.assertEqual(inc_dec.decrement(7), 3, "Should be 6")

    def inc_def_example(self):
        #This is not correctly named to be recognized as a test.
        self.assertEqual(inc_dec.increment(5), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()