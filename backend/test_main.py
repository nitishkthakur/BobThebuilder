import unittest
from main import your_function_name

class TestYourFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(your_function_name(args), expected_result)

if __name__ == '__main__':
    unittest.main()