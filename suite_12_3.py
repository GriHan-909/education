import unittest
import tests_12_3

tournamST = unittest.TestSuite()
tournamST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tournamST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournamST)