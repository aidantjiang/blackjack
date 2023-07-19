import pygame
from pygame import mixer

from visualization.deck import Deck
from visualization.button import Button

deck = Deck()

def main():
    pygame.init()
    mixer.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    pygame.display.set_caption('blackjack')
    pygame.display.set_icon(deck.cardBacks[1])
    
    deck._deal_initial_cards()

    #COLORS
    DARK_BLUE = (43, 65, 98)
    BLUE_GREY = (56, 95, 113)
    OFF_WHITE = (245, 240, 246)
    LIGHT_BROWN = (215, 179, 119)
    DARK_BROWN = (143, 117, 79)

    running = True

    #BUTTONS
    def hit():
        deck._get_card('player')
        click.play()
    def stay():
        print('stay')
    buttons = []
    button_width = 100
    button_height = 40
    hit_button_x = ((screen_width - button_width) // 2) - button_width // 2 - 10
    hit_button_y = (screen_height - button_height) // 2
    stay_button_x = ((screen_width - button_width) // 2) + button_width // 2 + 10
    stay_button_y = (screen_height - button_height) // 2
    hit_button = Button(hit_button_x, hit_button_y, button_width, button_height, "hit", hit)
    stay_button = Button(stay_button_x, stay_button_y, button_width, button_height, "stay", stay)
    buttons.extend([hit_button, stay_button])

    #TILE
    pattern_image = pygame.image.load("public/pattern.png")
    pattern_image = pygame.transform.scale(pattern_image, (pattern_image.get_width() / 6, pattern_image.get_height() / 6))
    pattern_width, pattern_height = pattern_image.get_size()

    #SOUND EFFECTS
    click = pygame.mixer.Sound('public/sounds/click_high.wav')
    click.set_volume(0.1)

    while (running):
        dealer_cards = deck.dealerCards
        player_cards = deck.playerCards

        #CARD VARIABLES
        padding = 10
        player_card_delay = 10 + (20 * (len(player_cards) - 1))
        dealer_card_delay = 10

        screen.fill(BLUE_GREY)
        for x in range(0, screen_width, pattern_width):
                for y in range(0, screen_height, pattern_height):
                    screen.blit(pattern_image, (x, y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for button in buttons:
                button.handle_event(event)
        # SHOW BUTTONS
        for button in buttons:
            button.draw(screen)

        # SHOW DEALER CARDS
        for card in dealer_cards:
            screen.blit(card, (padding, 10))
            dealer_card_delay += 20
        screen.blit(deck.cardBacks[0], (dealer_card_delay, 10))

        # SHOW PLAYER CARDS
        for card in player_cards:
            screen.blit(card, (screen_width - player_card_delay - card.get_width(), screen_height - padding - card.get_height()))
            player_card_delay -= 20
        pygame.display.flip()

if __name__ == "__main__":
    main()