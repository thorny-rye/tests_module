import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'ok')
    def test_walk(self):
        test_name = runner.Runner("Gena")
        count = 0
        while count != 10:
            count += 1
            test_name.walk()
        self.assertEqual(test_name.distance, 50)

    @unittest.skipIf(is_frozen, 'ok')
    def test_run(self):
        test_name = runner.Runner("Gena")
        count = 0
        while count != 10:
            count += 1
            test_name.run()
        self.assertEqual(test_name.distance, 100)

    @unittest.skipIf(is_frozen, 'ok')
    def test_challenge(self):
        test_name1 = runner.Runner("Gena")
        test_name2 = runner.Runner("Kirill")
        count = 0
        while count != 10:
            count += 1
            test_name1.run()
            test_name2.walk()
        self.assertNotEqual(test_name1.distance, test_name2.distance)
