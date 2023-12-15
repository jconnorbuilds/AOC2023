import re

def extract_numbers(str):
  return re.findall(r'\d', str)

def get_two_digit_num(num_string):
  digit1, digit2 = num_string[0], num_string[-1]
  return int(digit1 + digit2)

def parse_strings(path_to_txt_file):
  total = 0
  with open(path_to_txt_file) as file:
    for line in file:
      numbers = extract_numbers(line)
      two_digit_number = get_two_digit_num(numbers)
      total += two_digit_number

  return total

input_strings = 'input.txt'
answer = parse_strings(input_strings)
print(answer)