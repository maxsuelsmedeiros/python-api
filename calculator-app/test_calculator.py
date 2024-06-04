import unittest

from calculator import calculator
class TestCalculator(unittest.TestCase):

    def test_operation_none(self):
        with self.assertRaises(Exception) as ex:
            calculator(None,2,2)
        self.assertEqual(ex.exception.args[0], second="Operation can't be None.")

if __name__=='__main__':
    unittest.main()
