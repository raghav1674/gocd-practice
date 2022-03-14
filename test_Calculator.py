import unittest
from unittest.mock import patch
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    # each class
    @classmethod
    def setUpClass(cls):
        # print('setUpClass')
        pass

    # each class
    @classmethod
    def tearDownClass(cls):
        # print('tearDownClass')
        pass

    # every test fn.
    def setUp(self):
        # print('setUp')
        self.a = 1
        self.b = 2

    # every test fn.
    def tearDown(self):
        # print('tearDown')
        pass

    def test_add(self):
        self.assertEqual(Calculator.add(self.a, self.b), 3)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(self.a, self.b), -1)

    def test_divide(self):
        self.assertEqual(Calculator.divide(self.a, self.b), 0)
        self.assertRaises(ValueError, Calculator.divide, 2, 0)

    def test_mulitply(self):
        self.assertEqual(Calculator.mulitply(self.a, self.b), 2)

    # mock

    def test_calculator_api(self):
        with patch('Calculator.requests.post') as mocked_post:
            mocked_post.return_value.json = lambda: {
                'error': None, 'result': ['3']}
            self.assertEqual(Calculator.calculator_api(1, 2), 3)
            mocked_post.return_value.json = lambda: {
                'error': 'Wrong Expression', 'result': []}
            self.assertEqual(Calculator.calculator_api(1, ')'),
                             'Bad Request')


if __name__ == '__main__':
    unittest.main()
