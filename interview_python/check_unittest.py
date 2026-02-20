import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_a(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(3, 4), 7)


if __name__ == "__main__":
    unittest.main()