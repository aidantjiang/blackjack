import pygame, random

class Deck:
    def __init__(self):
        self.deck = [] #deck of card images (data will look like this: [(value, Surface), ...])
        # example: [(3, Surface), (10, Surface)] # 3, King
        self.cardBacks = [] # red and blue card back images (data looks like this: [Surface, Surface])
        self.setDeck()
        self.scaleCardImages()
        self.shuffle()
    def setDeck(self):
        path = './public/cards/'
        suits = ['spade', 'club', 'diamond', 'heart']
        card_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for suit in suits:
            for value in card_nums:
                image_path = f'{path}{suit}{value}.png'
                image = pygame.image.load(image_path)
                self.deck.append((card_values[card_nums.index(value)], image))
        self.cardBacks.append(pygame.image.load(f'{path}cardback_blue.png'))
        self.cardBacks.append(pygame.image.load(f'{path}cardback_red.png'))
    def scaleCardImages(self):
        # deck
        scaled_deck = []
        for card in self.deck:
            card_width = card[1].get_width()
            card_height = card[1].get_height()
            scaled_card = pygame.transform.scale(card[1], (card_width * 2, card_height * 2))
            new_tuple = (self.deck[self.deck.index(card)][0], scaled_card)
            scaled_deck.append(new_tuple)
        self.deck = scaled_deck
        #backs
        scaled_cardBacks = []
        for card in self.cardBacks:
            card_width = card.get_width()
            card_height = card.get_height()
            scaled_card = pygame.transform.scale(card, (card_width * 2, card_height * 2))      
            scaled_cardBacks.append(scaled_card)
        self.cardBacks = scaled_cardBacks
    def shuffle(self):
        random.shuffle(self.deck)