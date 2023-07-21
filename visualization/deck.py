import pygame, random

class Deck:
    def __init__(self):
        self.first_creation = True

        self.deck = [] #deck of card images (data will look like this: [(value, Surface), ...])
        self.drawnCards = []
        # example: [(3, Surface), (10, Surface)] # 3, King
        self.cardBacks = [] # red and blue card back images (data looks like this: [Surface, Surface])
        self.agentCards = []
        self._create_deck()
    def _create_deck(self):
        # vars and consts
        if (self.first_creation):
            path = './public/cards/'
            suits = ['spade', 'club', 'diamond', 'heart']
            card_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
            card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            final_deck = []
            final_cardbacks = []

            #set initial deck and cardback values
            for suit in suits:
                for value in card_nums:
                    image_path = f'{path}{suit}{value}.png'
                    image = pygame.image.load(image_path)
                    final_deck.append((card_values[card_nums.index(value)], image))
            final_cardbacks.append(pygame.image.load(f'{path}cardback_blue.png'))
            final_cardbacks.append(pygame.image.load(f'{path}cardback_red.png'))

            #scale image sizes
            # deck
            scaled_deck = []
            for card in final_deck:
                card_width = card[1].get_width()
                card_height = card[1].get_height()
                scaled_card = pygame.transform.scale(card[1], (card_width * 2, card_height * 2))
                new_tuple = (final_deck[final_deck.index(card)][0], scaled_card)
                scaled_deck.append(new_tuple)
            final_deck = scaled_deck
            #backs
            scaled_cardBacks = []
            for card in final_cardbacks:
                card_width = card.get_width()
                card_height = card.get_height()
                scaled_card = pygame.transform.scale(card, (card_width * 2, card_height * 2))      
                scaled_cardBacks.append(scaled_card)
            final_cardbacks = scaled_cardBacks

            #shuffle
            random.shuffle(final_deck)

            #set class vars
            self.deck = final_deck
            self.cardBacks = final_cardbacks
            self.first_creation = False
        else:
            self.deck.extend(self.drawnCards)
            self.drawnCards =[]
            # random.shuffle(self.deck) DO NOT USE, REALLY SLOW WITH TUPLES
            shuffled_deck = random.sample(self.deck, len(self.deck))
            self.deck = [card_tuple for card_tuple in shuffled_deck]

    def _get_card(self):
        if len(self.deck) == 0:
            self._create_deck()
        card = self.deck.pop(0)

        self.drawnCards.append(card)
        return card # type (num, surface)
    
    def _deal_initial_cards(self):
        # initial cards -- one to dealer, two to player
        value1, surface1 = self._get_card()
        value2, surface2 = self._get_card()
        value3, surface3 = self._get_card()

        #for gym env
        player_sum = value1 + value2
        dealer_sum = value3
        usable_ace = 1 if value1 == 11 or value2 == 11 else 0
        #dealer cannot use aces

        #for pygame env
        surfaces = []
        surfaces.extend([surface1, surface2, surface3])


        return surfaces, player_sum, dealer_sum, usable_ace