import pygame

class Transition:
    def __init__(self):
        self.images = {}
        self._load()
    def _load(self):
        self.images['dealer_bust'] = pygame.image.load('./public/dealer-bust.png')
        self.images['player_bust'] = pygame.image.load('./public/player-bust.png')
        self.images['robot_bust'] = pygame.image.load('./public/robot-bust.png')
        self.images['dealer_turn'] = pygame.image.load('./public/dealer-turn.png')
        self.images['dealer_wins'] = pygame.image.load('./public/dealer-wins.png')
        self.images['player_wins'] = pygame.image.load('./public/player-wins.png')
        self.images['robot_win'] = pygame.image.load('./public/robot-win.png')

        