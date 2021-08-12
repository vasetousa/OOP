from unittest import TestCase, main
from Code_testing_Unittests.Tests.cat import Cat


class CatTests(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Luis")

    def test_is_cat_size_increased_after_eat_method(self):

        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_is_cat_fed_status_after_eat_method(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_exception_raised_if_cat_is_fed_after_eat_method(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_exception_raised_if_cat_tries_to_sleep_when_not_fed(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_not_sleepy_after_sleep_method(self):
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()