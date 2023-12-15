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

    def __str__(self):
        return f"{self.number}, line: {self.line_number}, bounds: ({self.topleft_x}, {self.topleft_y}),({self.bottomright_x},{self.bottomright_y}), {self.is_a_part}"

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
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name}, ({self.x} , {self.y})"


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
            Symbol(symbol.group(), symbol.span()[0], self.id)
            for symbol in re.finditer(r"[@#$%&+*-]", line)
        ]


def populate_symbols_and_parts():
    symbols = []
    potential_parts = []
    with open("day3.txt") as f:
        for i, line in enumerate(f):
            [
                symbols.append(Symbol(symbol.group(), symbol.span()[0], i))
                for symbol in list(re.finditer(r"[@#=$%/&+*-]", line))
            ]
            l = Line(line, i)
            potential_parts.extend(l.potential_parts)
    return symbols, potential_parts


if __name__ == "__main__":
    total = 0
    symbols, potential_parts = populate_symbols_and_parts()
    for p in potential_parts:
        if p.scan_for_all_symbols(symbols):
            total += p.number

    print(total)
