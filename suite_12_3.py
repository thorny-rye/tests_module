import unittest
import tests_12_1
import tests_12_2


runTS = unittest.TestSuite()
runTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
runTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runTS)