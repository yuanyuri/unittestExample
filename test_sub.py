from calculator import Count
import unittest


class TestSub(unittest.TestCase):

    def setUp(self):
        print("test substract setup")

    def tearDown(self):
        print("test completed")

    def test_sub1(self):
        t = Count(11, 1)
        self.assertEqual(t.sub(), 10)

    def test_sub2(self):
        t = Count(1, 1)
        self.assertEqual(t.sub(), 0)

if __name__ == '__main__':
    unittest.main()
