from unittest import TestCase, main

from Code_testing_Unittests.Tests.Paint_Factory.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.pf = PaintFactory("Panda", 100)

    def test_init(self):
        pf = PaintFactory("Panda", 100)
        self.assertEqual("Panda", pf.name)
        self.assertEqual(100, pf.capacity)
        self.assertEqual({}, pf.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], pf.valid_ingredients)

    def test_add_ingredient_product_type(self):
        with self.assertRaises(TypeError) as ex:
            self.pf.add_ingredient("purple", 1)
        self.assertEqual("Ingredient of type purple not allowed in PaintFactory", str(ex.exception))
        self.assertEqual({}, self.pf.ingredients)
        self.pf.add_ingredient("white", 10)
        self.assertEqual({"white": 10}, self.pf.ingredients)

    def test_add_ingredient_quantity(self):
        with self.assertRaises(ValueError) as ex:
            self.pf.add_ingredient("white", 101)
        self.assertEqual("Not enough space in factory", str(ex.exception))
        self.assertEqual({}, self.pf.ingredients)
        self.pf.add_ingredient("white", 10)
        self.assertEqual({"white": 10}, self.pf.ingredients)

    def test_add_ingredient_quantity_increases(self):
        self.assertEqual({}, self.pf.ingredients)
        self.pf.add_ingredient("white", 10)
        self.assertEqual({"white": 10}, self.pf.ingredients)
        self.pf.add_ingredient("white", 10)
        self.assertEqual({"white": 20}, self.pf.ingredients)

    def test_remove_ingredient(self):
        self.assertEqual({}, self.pf.ingredients)
        with self.assertRaises(KeyError) as ex:
            self.pf.remove_ingredient("white", 10)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))
        self.pf.add_ingredient("white", 10)
        self.pf.remove_ingredient("white", 5)
        self.assertEqual({"white": 5}, self.pf.ingredients)

    def test_remove_ingredient_invalid_quantity(self):
        self.pf.add_ingredient("white", 1)
        self.assertEqual({"white": 1}, self.pf.ingredients)
        with self.assertRaises(ValueError) as ex:
            self.pf.remove_ingredient("white", 3)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_return_ingredients(self):
        self.pf.add_ingredient("white", 10)
        self.assertEqual({"white": 10}, self.pf.products)



if __name__ == "__main__":
    main()