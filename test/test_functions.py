import unittest
from main import camper_age_input

class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(60, camper_age_input.convert_to_months(5))
        self.assertEqual(36, camper_age_input.convert_to_months(3))
        self.assertEqual(24, camper_age_input.convert_to_months(2))
        self.assertEqual(12, camper_age_input.convert_to_months(1))

if __name__ == '__main__':
    unittest.main()
