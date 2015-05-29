import unittest
from psn import Panda
from psn import PandaSocialNetwork


class psnTest(unittest.TestCase):

    def setUp(self):
        self.panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.psn = PandaSocialNetwork()

    def test_create_new_panda_class(self):
        self.assertTrue(isinstance(self.panda, Panda))

    def test_name_for_panda(self):
        self.assertEqual(self.panda.name(), "Ivo")

    def test_email_for_panda(self):
        self.assertEqual(self.panda.email(), "ivo@pandamail.com")

    def test_gender_for_panda(self):
        self.assertEqual(self.panda.gender(), "male")

    def test_isMale_for_panda(self):
        self.assertEqual(self.panda.isMale(), True)

    def test_isFemale_for_panda(self):
        self.assertEqual(self.panda.isFemale(), False)

    def test_str_dunder_for_panda(self):
        self.assertEqual(str(self.panda), "I am Ivo, I am male, pm me: ivo@pandamail.com")

    def test_eq_dunder_for_same_pandas(self):
        panda1 = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(self.panda, panda1)

    def test_eq_dunder_for_pandas_with_different_names(self):
        panda1 = Panda("Rado", "ivo@pandamail.com", "male")
        self.assertNotEqual(self.panda, panda1)

    def test_eq_dunder_for_pandas_with_different_emails(self):
        panda1 = Panda("Ivo", "rado@pandamail.com", "male")
        self.assertNotEqual(self.panda, panda1)

    def test_eq_dunder_for_pandas_with_different_genders(self):
        panda1 = Panda("Ivo", "ivo@pandamail.com", "female")
        self.assertNotEqual(self.panda, panda1)

    def test_hash_dunder_for_same_pandas(self):
        panda1 = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(hash(self.panda), hash(panda1))

    def test_hash_dunder_for_different_pandas(self):
        panda1 = Panda("Ivo ", "ivo@pandamail.com", "male")
        self.assertNotEqual(hash(self.panda), hash(panda1))

    def test_value_error_raises_from_invalid_gender(self):
        with self.assertRaises(ValueError):
            panda1 = Panda("Ivo", "ivo@pandamail.com", "camel")

    def test_index_with_more_than_one_at(self):
        panda1 = Panda("Ivo", "ivo@panda@mail.com", "male")
        self.assertEqual(panda1.get_index(), 3)

    def test_has_no_special_symbols_true(self):
        self.assertTrue(self.panda.has_no_special_symbols())

    def test_has_no_special_symbols_false(self):
        panda1 = Panda("Ivo", "i-vo@panda@mail.com", "male")
        self.assertFalse(panda1.has_no_special_symbols())

    def test_has_dot_after_at(self):
        self.assertTrue(self.panda.has_dot())

    def test_has_not_dot_after_at(self):
        panda1 = Panda("Ivo", "ivo@panda@mailcom", "male")
        self.assertFalse(panda1.has_dot())

    def test_has_dots_after_at(self):
        panda1 = Panda("Ivo", "ivo@panda@.mailcom.", "male")
        self.assertFalse(panda1.has_dot())

    def test_has_no_symbols_after_at(self):
        panda1 = Panda("Ivo", "ivopanda@", "male")
        self.assertFalse(panda1.no_symbols())

    def test_has_symbols_after_at(self):
        self.assertTrue(self.panda.no_symbols())

    def test_create_new_psn_class(self):
        self.assertTrue(isinstance(self.psn, PandaSocialNetwork))

    def test_add_panda_for_psn(self):
        self.psn.add_panda(self.panda)
        self.assertEqual(self.psn[self.panda], [])

if __name__ == '__main__':
    unittest.main()
