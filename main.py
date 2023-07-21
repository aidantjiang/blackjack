import pygame
from pygame import mixer

from visualization.transition import Transition
from visualization.button import Button
from visualization.game import deck

from agents.player_agent import Player
from agents.dealer_agent import Dealer
initial_cards, player_sum, dealer_sum, ace = deck._deal_initial_cards()

#declare agents
dealer = Dealer(dealer_sum, initial_cards[2])
player = Player(player_sum, [initial_cards[0], initial_cards[1]], ace)

#declare other classes
transition_player = Transition()
dealer_bust_img = transition_player.images['dealer_bust']
player_bust_img = transition_player.images['player_bust']
robot_bust_img = transition_player.images['robot_bust']
dealer_turn_img = transition_player.images['dealer_turn']
dealer_wins_img = transition_player.images['dealer_wins']
player_wins_img = transition_player.images['player_wins']
robot_win_img = transition_player.images['robot_win']

def main():
    pygame.init()
    mixer.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    pygame.display.set_caption('blackjack')
    pygame.display.set_icon(deck.cardBacks[1])

    #COLOR PALLATE
    DARK_BLUE = (43, 65, 98)
    BLUE_GREY = (56, 95, 113)
    OFF_WHITE = (245, 240, 246)
    LIGHT_BROWN = (215, 179, 119)
    DARK_BROWN = (143, 117, 79)

    running = True

    #BUTTONS
    def hit():
        player._move('hit')
        click.play()
    def stay():
        player._move('stay')
        click.play()
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
    click.set_volume(0.5)

    while (running):
        dealer_cards = dealer.cards
        player_cards = player.cards

        # CARD VARIABLES
        padding = 10
        player_card_delay = 10 + (20 * (len(player_cards) - 1))
        dealer_card_delay = 10

        screen.fill(BLUE_GREY)
        for x in range(0, screen_width, pattern_width):
                for y in range(0, screen_height, pattern_height):
                    screen.blit(pattern_image, (x, y))

        # PYGAME EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(dealer.cards)
                running = False
            for button in buttons:
                button.handle_event(event)

        # SHOW BUTTONS
        for button in buttons:
            button.draw(screen)

        #DEAL CARDS FOR DEALER?
        if (player.done):
            if (not dealer.stop):
                dealer._move('hit')

        # SHOW DEALER CARDS
        for card in dealer_cards:
            screen.blit(card, (dealer_card_delay, 10))
            dealer_card_delay += 20
        if (len(dealer_cards) < 2):
            screen.blit(deck.cardBacks[0], (dealer_card_delay, 10))

        # SHOW PLAYER CARDS
        for card in player_cards:
            screen.blit(card, (screen_width - player_card_delay - card.get_width(), screen_height - padding - card.get_height()))
            player_card_delay -= 20
        pygame.display.flip()

if __name__ == "__main__":
    main()