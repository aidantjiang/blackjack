from visualization.game import deck

import time

class Dealer:
    def __init__(self, total, initial_cards):
        self.total = total
        self.cards = [initial_cards]
        self.stop = False
    def _reset(self, total, initial_cards):
        self.total = total
        self.cards = [initial_cards]
        self.stop = False
    def _move(self, type):
        if (type == 'hit'):
            if (not self.stop):
                num, surface = deck._get_card()
                self.total += num
                self.cards.append(surface)
                if (self.total >= 17):
                    self.stop = True
                    if (self.total > 21):
                        #code here
                        pass
        time.sleep(0.6)