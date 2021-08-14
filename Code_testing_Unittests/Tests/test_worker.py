from unittest import TestCase, main
from Code_testing_Unittests.Tests.worker import Worker


class WorkerTests(TestCase):
    def test_is_worker_initialised_with_all_attributes(self):
        name = "Gosho"
        salary = 1200
        energy = 100
        worker = Worker(name, salary, energy)
        self.assertEqual(name, worker.name)
        self.assertEqual(salary, worker.salary)
        self.assertEqual(energy, worker.energy)
        self.assertEqual(0, worker.money)

    def test_is_energy_incremented_after_rest_method(self):
        name = "Gosho"
        salary = 1200
        energy = 100
        worker = Worker(name, salary, energy)
        worker.rest()
        self.assertEqual(energy + 1, worker.energy)

    def test_is_Exception_raised_when_worker_tries_to_work_when_negative_or_0_energy(self):
        name = "Gosho"
        salary = 1200
        energy = 0
        worker = Worker(name, salary, energy)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_is_money_increased_by_salary_after_work_method(self):
        name = "Gosho"
        salary = 1200
        energy = 100
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(salary, worker.money)

    def test_is_energy_decreased_after_work_method(self):
        name = "Gosho"
        salary = 1200
        energy = 100
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(energy - 1, worker.energy)

    def test_is_info_presented_after_method_get_info(self):
        name = "Gosho"
        salary = 1200
        energy = 100
        worker = Worker(name, salary, energy)
        actual_result = worker.get_info()
        expected_result = f'{name} has saved {worker.money} money.'
        self.assertEqual(actual_result, expected_result)



if __name__ == '__main__':
    main()
