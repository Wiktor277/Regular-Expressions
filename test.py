import unittest


import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print("Setting up test cases")

    def test_do_staff(self):
        test_param = 10
        result = main.do_staff(test_param)
        self.assertEqual(result, test_param + 5)


    def test_do_staff2(self):
        test_param = 'stgrw'
        result = main.do_staff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_staff3(self):
        test_param = None
        result = main.do_staff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_staff4(self):
        test_param = ''
        result = main.do_staff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def tearDown(self):
        print("Tearing down test cases")

    if __name__ == "__main__":
        unittest.main()


