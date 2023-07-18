import pygame

from visualization.deck import Deck
from visualization.button import Button

deck = Deck()

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    pygame.display.set_caption('blackjack')
    pygame.display.set_icon(deck.cardBacks[1])
    
    cards, _, _, _ = deck._deal_initial_cards()

    #COLORS
    DARK_BLUE = (43, 65, 98)
    BLUE_GREY = (56, 95, 113)
    OFF_WHITE = (245, 240, 246)
    LIGHT_BROWN = (215, 179, 119)
    DARK_BROWN = (143, 117, 79)

    running = True

    #BUTTONS
    def button_click():
        print('hit')
    buttons = []
    button_width = 100
    button_height = 40
    button_x = (screen_width - button_width) // 2
    button_y = (screen_height - button_height) // 2
    my_button = Button(button_x, button_y, button_width, button_height, "hit", button_click)
    buttons.append(my_button)

    while (running):
        screen.fill(DARK_BLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for button in buttons:
                button.handle_event(event)
        for button in buttons:
            button.draw(screen)
        screen.blit(deck.deck[20][1], (10, 10))
        screen.blit(deck.cardBacks[0], (30, 10))
        screen.blit(cards[2], (screen_width - 30 - cards[2].get_width(), screen_height - 10 - cards[2].get_height()))
        screen.blit(cards[0], (screen_width - 10 - cards[0].get_width(), screen_height - 10 - cards[0].get_height()))
        pygame.display.flip()

if __name__ == "__main__":
    main()