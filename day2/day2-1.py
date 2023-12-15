starting_cubes = {"red": 12, "green": 13, "blue": 14}


class Round:
    def __init__(self, round_string):
        self.round_string = round_string
        self.scores = self.get_scores()
        self.is_feasible = self.check_for_feasibility()

    def __str__(self):
        return " ".join(self.scores)

    def get_scores(self):
        hand = self.round_string.split(", ")
        return {cubes.split(" ")[1].strip(): int(cubes.split(" ")[0]) for cubes in hand}

    def check_for_feasibility(self):
        return all(
            self.scores[color] <= starting_cubes.get(color, 0) for color in self.scores
        )


class Game:
    def __init__(self, game_string):
        self.game_string = game_string
        self.id = int(self.game_string.split(" ")[1][0:-1])
        self.rounds = self.get_rounds()
        self.is_feasible = self.determine_feasibility()

    def get_rounds(self):
        rounds_string = self.game_string.split(": ")[1].split("; ")
        return [Round(r) for r in rounds_string]

    def determine_feasibility(self):
        return all(r.is_feasible for r in self.rounds)


total = 0
with open("day2/day2.txt") as f:
    for game in f:
        g = Game(game)
        if g.is_feasible:
            total += g.id
print(total)
