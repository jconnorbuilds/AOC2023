import re


class Potential_Part:
    def __init__(self, number, idxs, line_number):
        self.number = int(number)
        self.line_number = line_number
        self.number_left_bound, self.number_right_bound = idxs
        (
            self.topleft_x,
            self.topleft_y,
            self.bottomright_x,
            self.bottomright_y,
        ) = self.get_boundary()

    def get_boundary(self):
        start_idx, stop_idx = self.number_left_bound, self.number_right_bound - 1
        top_left = start_idx - 1, self.line_number - 1
        bottom_right = stop_idx + 1, self.line_number + 1
        return top_left[0], top_left[1], bottom_right[0], bottom_right[1]

    def scan_for_symbol(self, x, y):
        return (
            x >= self.topleft_x
            and x <= self.bottomright_x
            and y >= self.topleft_y
            and y <= self.bottomright_y
        )

    def print_boundary(self):
        print(
            f"boundary: ({self.topleft_x}, {self.topleft_y}), ({self.bottomright_x}, {self.bottomright_y})"
        )

    def scan_for_all_symbols(self, symbols):
        return any(self.scan_for_symbol(symbol.x, symbol.y) for symbol in symbols)


class Symbol:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x[0]
        self.y = y

    def get_boundary(self):
        top_left = self.x - 1, self.y - 1
        bottom_right = self.x + 1, self.y + 1
        return top_left[0], top_left[1], bottom_right[0], bottom_right[1]

    def get_surrounding_parts(self, all_parts):
        return [part for part in all_parts if part.scan_for_symbol(self.x, self.y)]


class Line:
    def __init__(self, string, i):
        self.id = i
        self.potential_parts = self.get_potential_parts(string)
        self.symbols = self.get_symbols(string)

    def get_potential_parts(self, line):
        """
        Potential Parts are groups of numbers, i.e. "467", "114", etc.

        line: A line of the input string
        returns: a list of Potential Part objects from a line of the input string.
        """
        return [
            Potential_Part(num.group(), num.span(), self.id)
            for num in re.finditer(r"\b(\d+)\b", line)
        ]

    def get_symbols(self, line):
        """
        A Symbol within the boundary of a Potential Part makes that
        Potential Part an actual Part.

        line: A line of the input string
        returns: a list of Symbol objects from a line of the input string.
        """
        return [
            Symbol(symbol.group(), symbol.span(), self.id)
            for symbol in re.finditer(r"[@#$%&+*-]", line)
        ]


def extract_matches(pattern, text, obj):
    return [
        obj(match.group(), match.span(), i)
        for i, line in enumerate(text)
        for match in re.finditer(pattern, line)
    ]


def populate_symbols_and_parts():
    with open("day3/day3.txt") as (f):
        lines = f.readlines()
    symbols = extract_matches(r"[@#=$%/&+*-]", lines, Symbol)
    potential_parts = extract_matches(r"\b(\d+)\b", lines, Potential_Part)

    return symbols, potential_parts


if __name__ == "__main__":
    total = 0
    gear_ratio = 0
    symbols, potential_parts = populate_symbols_and_parts()
    for p in potential_parts:
        if p.scan_for_all_symbols(symbols):
            total += p.number

    for symbol in symbols:
        if symbol.name == "*":
            surrounding_parts = symbol.get_surrounding_parts(potential_parts)
            if len(surrounding_parts) >= 2:
                ttl = 1
                for part in surrounding_parts:
                    ttl *= part.number
                gear_ratio += ttl

    print(total)
    print(f"Gear ratio: {gear_ratio}")
