import unittest
from exercise03_erin import *

class exerciseTests(unittest.TestCase):
    
    def test_vowels(self):
        self.assertEqual(4, count_vowels("mississippi"))
        with self.assertRaises(TypeError): count_vowels(5)
        with self.assertRaises(TypeError): count_vowels([1,2,3])

if __name__ == '__main__':
  unittest.main()

