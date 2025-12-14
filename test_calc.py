# test_calc.py
import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        # The robot will check: Does 2 + 3 actually equal 5?
        result = calc.add(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
