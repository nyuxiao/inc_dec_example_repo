import unittest
import inc_dec   # The code to test

class ClassDiffPattern(unittest.TestCase):

    def test_a1(self):
        print("test_inc hello")
        self.assertEqual(inc_dec.increment(5), 6, "Should be 6")

    def not_found_test(self):
        self.assertEqual(inc_dec.decrement(7), 3, "Should be 6")