import re

number_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def extract_num_digits(str):
    pass
    return re.findall(r"\d", str)


def create_rexp(string):
    return rf"(?:{string})"


def extract_num_words(input_str):
    word_list = []
    number_words = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for word in number_words:
        instances = re.findall(rf"(?:{word})", input_str)
        if len(instances) > 0:
            word_list += instances
    return word_list


def get_two_digit_num(input_str, nums_list):
    digit1 = get_val_with_lowest_idx(input_str, nums_list)
    digit2 = get_val_with_highest_idx(input_str, nums_list)
    return int(digit1 + digit2)


def find_indecies(input_str, num):
    idxs = [m.start() for m in re.finditer(num, input_str)]
    return idxs


def parse_strings(path_to_txt_file):
    total = 0
    with open(path_to_txt_file) as file:
        for line in file:
            numbers_list = extract_num_digits(line)
            numbers_list += extract_num_words(line)
            two_digit_number = get_two_digit_num(line, numbers_list)
            total += two_digit_number

    return total


def parse_string(string):
    numbers_list = extract_num_digits(string)
    numbers_list += extract_num_words(string)


def get_val_with_lowest_idx(input_str, nums_list):
    lowest_idx = len(input_str)
    value_at_lowest_idx = ""
    for num in nums_list:
        idxs = find_indecies(input_str, num)
        if idxs[0] < lowest_idx:
            lowest_idx = idxs[0]
            value_at_lowest_idx = num

    return parse_value(value_at_lowest_idx)


def get_val_with_highest_idx(input_str, nums_list):
    highest_idx = 0
    value_at_highest_idx = ""
    for num in nums_list:
        idxs = find_indecies(input_str, num)
        if idxs[-1] >= highest_idx:
            highest_idx = idxs[-1]
            value_at_highest_idx = num

    return parse_value(value_at_highest_idx)


def parse_value(value):
    if value in [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]:
        return str(number_words[value])
    else:
        return str(value)


input_strings = "day1/input.txt"
answer = parse_strings(input_strings)
print(answer)
