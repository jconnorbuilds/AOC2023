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
  def __repr__(self):
    return str(f"#{self.card_number}")
  
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

def get_matches(cards, start_idx):
  match_cards = []
  print(cards)
  for i in range(start_idx, len(cards)):
    card = cards[i]
    for j in range(1, card.number_of_matches + 1):
      match_cards.append(cards[i+j])
      print(f"card: {card}, match: {cards[i+j]}")
  return match_cards

def get_matches_for_idx(orig_cards, all_cards, idx):
  matches = []
  for j in range(0, len(orig_cards)):
    if orig_cards[j] == all_cards[idx]:
      for i in range(1, orig_cards[j].number_of_matches + 1):
        print(i, orig_cards[j].number_of_matches)
        matches.append(orig_cards[j+i])
  return matches


if __name__ == "__main__":
  total = 0
  orig_cards = [Card(line) for line in lines]
  all_cards = []
  for ocard in orig_cards:
    all_cards.append(ocard)
  for acard in all_cards:
    i = 1
    print(f"acard: {acard.card_number}, matches: {acard.number_of_matches}")
    while i <= acard.number_of_matches:
      all_cards.append(orig_cards[acard.card_number-1 + i])
      # print(f"append {orig_cards[acard.card_number -1 + i]}")
      all_cards.sort(key=lambda card: card.card_number)
      i += 1

  print(len(all_cards))

  print("done") 
  

