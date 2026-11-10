import unittest
from app import to_upper

class MyTestCase(unittest.TestCase):

    def test_to_upper(self):
        name = "Charan"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "CHARAN")

if __name__ == "__main__":
    unittest.main()