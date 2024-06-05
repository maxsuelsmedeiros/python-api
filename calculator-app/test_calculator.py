import unittest

from calculator import calculator
class TestCalculator(unittest.TestCase):

    def test_operation_none(self):
        with self.assertRaises(Exception) as ex:
            calculator(None,2,2)
        self.assertEqual(ex.exception.args[0], second="Operation can't be None.")
    
    def test_valid_number(self):
        with self.assertRaises(Exception) as ex:
            calculator('add',None,2)
        self.assertEqual(ex.exception.args[0], 'Need to inform 2 valid numbers.')
        with self.assertRaises(Exception) as ex:
            calculator('add',2,None)
        self.assertEqual(ex.exception.args[0], 'Need to inform 2 valid numbers.')

    def test_operation_isvalid(self):
        with self.assertRaises(Exception) as ex:
            calculator('fatorial',2,10)
        self.assertEqual(ex.exception.args[0], 'The operations can be add,sub,div or multiply.')

    def test_add(self):
        result: float = calculator('add',10,30)
        self.assertEqual(result,40)

    def test_sub(self):
        result: float = calculator('sub',30,10)
        self.assertEqual(result,20)

    def test_div(self):
        result: float = calculator('div',30,10)
        self.assertEqual(result,3)

    def test_multiply(self):
        result: float = calculator('multiply',5,8)
        self.assertEqual(result,40)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError) as zero_ex:
            calculator('div',0,0)
        self.assertEqual(zero_ex.exception.args[0],'You can\'t divide by zero.')

if __name__=='__main__':
    unittest.main()
