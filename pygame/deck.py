import pygame

class Deck:
    def __init__(self):
        self.deck = [] #deck of card images
        self.cardBack = [] # red and blue card back images
        self.loadImages()
    def loadImages(self):
        path = '/../public/cards/'
        suits = ['spade', 'club', 'diamond', 'heart']
        card_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        for suit in suits:
            for value in card_values:
                image_path = f'{path}{suit}{value}.png'
                image = pygame.image.load(image_path)
                self.deck.append(image)
        self.cardBack.append(f'{path}cardback_blue.png')
        self.cardBack.append(f'{path}cardback_red.png')