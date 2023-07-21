from visualization.game import deck

class Player:
    def __init__(self, total, initial_cards, usable_ace):
        self.total = total
        self.cards = initial_cards
        self.done = False
        self.usable_ace = usable_ace
    def _move(self, type):
        if (type == 'hit'):
            if (not self.done):
                num, surface = deck._get_card()
                if num == 11:
                    self.usable_ace += 1
                self.total += num
                self.cards.append(surface)
                if (self.total > 21):
                    if (self.usable_ace > 0):
                        self.usable_ace -= 1
                        self.total -= 10
                    else:
                        self.done = True
        elif (type == 'stay'): #type stay
            self.done = True
