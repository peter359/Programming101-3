import unittest
from bgweb import Histogram


class bgwebTest(unittest.TestCase):
    def setUp(self):
        self.h = Histogram()

    def test_count_for_none(self):
        self.assertTrue(self.h.count("Apache") == None)

    def test_get_dict(self):
        self.assertEqual(self.h.get_dict(), {})

    def test_add_new_key(self):
        self.h.add("Apache")
        self.assertEqual(self.h.get_dict(), {'Apache': 1})

    def test_add_key_already_there(self):
        self.h.add("Apache")
        self.h.add("Apache")
        self.assertEqual(self.h.get_dict(), {'Apache': 2})

    def test_count_for_one(self):
        self.h.add("Apache")
        self.assertEqual(self.h.count("Apache"), 1)

    def test_items(self):
        self.h.add("Apache")
        self.h.add("Apache")
        self.h.add("nginx")
        self.assertTrue(self.h.items() == [("Apache", 2), ("nginx", 1)] or self.h.items() == [("nginx", 1), ("Apache", 2)])

    def test_get_dict_2(self):
        self.h.add("Apache")
        self.h.add("Apache")
        self.h.add("nginx")
        self.assertEqual(self.h.get_dict(), {"Apache": 2, "nginx": 1})


if __name__ == '__main__':
    unittest.main()
