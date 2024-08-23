import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walking  = Runner('GREG')
        for _ in range(10):
            walking.walk()
        self.assertEqual(walking.distance, 50)

    def test_run(self):
        runner = Runner('Alex')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        walk_1 = Runner('Mike')
        run_2 = Runner('Piter')
        for _ in range(10):
            walk_1.walk()
            run_2.run()
        self.assertNotEqual(walk_1.distance, run_2.distance)

if __name__ == "__main__":
    unittest.main()