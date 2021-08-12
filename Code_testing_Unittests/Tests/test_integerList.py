from unittest import TestCase, main
from Code_testing_Unittests.Tests.list import IntegerList


class ListTests(TestCase):
    def setUp(self) -> None:
        self.intList = IntegerList(1, 2, 3, 4, 5)

    def test_init_create_all_atributes(self):
        self.assertEqual([1, 2, 3, 4, 5], self.intList.get_data())


    def test_init_takes_no_integers(self):
        self.intList = IntegerList("1", 2.1, 3.4)
        self.assertEqual([], self.intList.get_data())

    def test_is_element_added_to_the_list_after_method_add_must_be_integer(self):
        with self.assertRaises(Exception) as ex:
            self.intList.add('6')
        self.assertEqual("Element is not Integer", str(ex.exception))

        self.intList.add(6)
        self.assertEqual([1, 2, 3, 4, 5, 6], self.intList.get_data())

    def test_is_remove_index_if_valid_else_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.intList.remove_index(20)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.intList.remove_index(3)
        self.assertEqual([1, 2, 3, 5], self.intList.get_data())


    def test_get_specific_element_from_list_after_method_get(self):
        with self.assertRaises(Exception) as ex:
            self.intList.get(10)
        self.assertEqual("Index is out of range", str(ex.exception))

        result = self.intList.get(0)
        self.assertEqual(result, 1)
        self.assertEqual([1, 2, 3, 4, 5], self.intList.get_data())

    def test_insert_element_in_specified_index_return_error_if_not_valid_index_or_integer(self):
        with self.assertRaises(Exception) as ex:
            self.intList.insert(0, '100')
        self.assertEqual("Element is not Integer", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.intList.insert(10, 100)
        self.assertEqual("Index is out of range", str(ex.exception))

        self.intList.insert(0, 100)
        self.assertEqual([100, 1, 2, 3, 4, 5], self.intList.get_data())

    def test_if_biggest_number_is_returned(self):
        result = self.intList.get_biggest()
        self.assertEqual(5, result)

    def test_if_element_on_index_is_returned(self):
        result = self.intList.get_index(5)
        self.assertEqual(4, result)


if __name__ == "__main__":
    main()