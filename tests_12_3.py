import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walking  = Runner('GREG')
        for _ in range(10):
            walking.walk()
        self.assertEqual(walking.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Alex')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walk_1 = Runner('Mike')
        run_2 = Runner('Piter')
        for _ in range(10):
            walk_1.walk()
            run_2.run()
        self.assertNotEqual(walk_1.distance, run_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = Runner("Усэйн", 10)
        self.Andrey = Runner("Андрей", 4)
        self.Nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for i in cls.all_results.values():
            print(i)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tournament = Tournament(90, self.Usain, self.Nick)
        result = tournament.start()
        self.all_results['test_1'] = {key: str(value) for key, value in result.items()}
        last_plase = max(result)
        self.assertTrue(result[last_plase] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tournament = Tournament(90, self.Andrey, self.Nick)
        result = tournament.start()
        self.all_results['test_2'] = {key: str(value) for key, value in result.items()}
        last_plase = max(result)
        self.assertTrue(result[last_plase] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tournament = Tournament(90, self.Usain, self.Andrey, self.Nick)
        result = tournament.start()
        self.all_results['test_3'] = {key: str(value) for key, value in result.items()}
        last_plase = max(result)
        self.assertTrue(result[last_plase] == "Ник")

if __name__ == "__main__":
    unittest.main()