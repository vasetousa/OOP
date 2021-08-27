from unittest import TestCase, main

from rename_to_project_and_finish.people.child import Child
from rename_to_project_and_finish.rooms.room import Room


class TestRoom(TestCase):
    def setUp(self):
        name = "Gosho"
        budget = 1200
        member_count = 100
        self.room = Room(name, budget, member_count)


    def test_init_attributes_assign(self):
        name = "Gosho"
        budget = 1200
        member_count = 100
        self.assertEqual(name, self.room.family_name)
        self.assertEqual(budget, self.room.budget)
        self.assertEqual([], self.room.children)
        self.assertEqual(member_count, self.room.members_count)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_not_negative(self):
        name = "Gosho"
        budget = 1200
        member_count = 100
        self.room = Room(name, budget, member_count)
        with self.assertRaises(Exception) as ex:
            self.room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(ex.exception))
        self.room.expenses = 3
        self.assertEqual(3, self.room.expenses)

    def test_calculate_expenses_properly(self):
        self.assertEqual(0, self.room.expenses)
        c1 = Child(8, 1, 1)
        expected = 300
        self.room.calculate_expenses([c1])
        self.assertEqual(expected, self.room.expenses)



if __name__ == "__main__":
    main()