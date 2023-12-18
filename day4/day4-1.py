with open("day4/input.txt") as (f):
  lines = f.readlines()

class Card:
  def __init__(self, card_string):
    self.card_string = card_string
    (self.card_number, 
    self.winning_numbers,
    self.player_numbers) = self.process_card()
    self.number_of_matches = self.get_number_of_matches()
    self.score = self.get_score(self.number_of_matches)
  
  def process_card(self):
    card_number = int(self.card_string.split(":")[0][-3:])
    winning_numbers = [int(x) for x in self.card_string.split("|")[0].split(":")[1].split()]
    player_numbers = [int(x) for x in self.card_string.split("|")[1].split()]

    return card_number, winning_numbers, player_numbers

  def get_number_of_matches(self):
    count = 0
    for w in self.winning_numbers:
      for p in self.player_numbers:
        if p == w:
          count += 1
    return count
  
  @staticmethod
  def get_score(matches_count):
    if matches_count < 2:
      return matches_count
    else:
      return 2 ** (matches_count - 1)


if __name__ == "__main__":
  total = 0
  for line in lines:
    card = Card(line)
    print(f"matches: {card.number_of_matches}, score: {card.score}")
    total += card.score
  print(f"total: {total}")

