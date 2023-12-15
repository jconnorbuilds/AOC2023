import functools

starting_cubes = {"red": 12, "green": 13, "blue": 14}
COLORS = ["blue", "green", "red"]


class Round:
    def __init__(self, round_string):
        self.round_string = round_string
        self.color_values = Round.color_values(round_string)
        self.is_feasible = all(
            self.color_values[color] <= starting_cubes.get(color, 0)
            for color in self.color_values
        )
        for color in COLORS:
            setattr(self, color, self.color_values[color])

    @staticmethod
    def color_values(round_string):
        hand = round_string.split(", ")
        scores = {
            color.split(" ")[1].strip(): int(color.split(" ")[0]) for color in hand
        }
        color_values = {color: scores.get(color, 0) for color in COLORS}
        return color_values


class Game:
    def __init__(self, game_string):
        self.game_string = game_string
        self.id = int(self.game_string.split(" ")[1][0:-1])
        self.rounds = [Round(r) for r in self.game_string.split(": ")[1].split("; ")]
        self.is_feasible = all(r.is_feasible for r in self.rounds)

    def get_power(self):
        highest_counts = [
            max(getattr(r, color) for r in self.rounds) for color in COLORS
        ]
        return functools.reduce(lambda a, b: a * b, highest_counts)


total = 0
total_power = 0

with open("day2/day2.txt") as f:
    for i, game in enumerate(f):
        g = Game(game)
        total_power += g.get_power()
        if g.is_feasible:
            total += g.id

print(total)
print(total_power)
