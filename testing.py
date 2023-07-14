import numpy as np


def function():
    deck = [1,2] * 4
    np.random.shuffle(deck)
    return deck

print(function())