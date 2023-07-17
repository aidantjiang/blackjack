import pygame

from visualization.deck import Deck

def main():
    deck = Deck()
    print()

    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    pygame.display.set_caption('blackjack')
    pygame.display.set_icon(deck.cardBacks[1])

    #COLORS
    DARK_BLUE = (43, 65, 98)
    BLUE_GREY = (56, 95, 113)
    OFF_WHITE = (245, 240, 246)
    LIGHT_BROWN = (215, 179, 119)
    DARK_BROWN = (143, 117, 79)

    running = True

    while (running):
        screen.fill(LIGHT_BROWN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(deck.deck[0][1], (10, 10))
        screen.blit(deck.cardBacks[0], (30, 12))
        screen.blit(deck.deck[10][1], (screen_width - 30 - deck.deck[12][1].get_width(), screen_height - 12 - deck.deck[12][1].get_height()))
        screen.blit(deck.deck[37][1], (screen_width - 10 - deck.deck[37][1].get_width(), screen_height - 10 - deck.deck[37][1].get_height()))
        pygame.display.flip()

if __name__ == "__main__":
    main()