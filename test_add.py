from calculator import Count
import unittest


class TestAdd(unittest.TestCase):

    def setUp(self):
        print('test add setup')

    def tearDown(self):
        print('test add completed')

    def test_add1(self):
        t = Count(1, 2)
        self.assertEqual(t.add(), 3)

    def test_add2(self):
        t = Count(100, 10)
        self.assertEqual(t.add(), 110)

if __name__ == "__main__":
    unittest.main()

