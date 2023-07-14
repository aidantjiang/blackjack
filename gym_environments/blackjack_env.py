import gym
from gym import spaces
import numpy as np

class BlackjackEnv(gym.Env):
    def __init__(self):
        super(BlackjackEnv, self).__init__()

        self.action_space = spaces.Discrete(2)  # 0 for "stay" and 1 for "hit"
        self.observation_space = spaces.Tuple((
            spaces.Discrete(32),  # current sum range 0-32
            spaces.Discrete(11),  # dealer card
            spaces.Discrete(2)    # ace y/n
        ))

        self.deck = None
        self.player_sum = None
        self.dealer_sum = None
        self.usable_ace = None
        self.round_done = None

        # initialize envrion
        self.reset()
    def reset(self):
        self.deck = self._create_deck()
        self.player_sum, self.dealer_sum, self.usable_ace = self._deal_initial_cards()
        self.round_done = False


        # initial observation
        return self._get_observation()


    def step(self, action):
        assert self.action_space.contains(action), "Invalid action"


        if action == 1:  # "hit"
            self._deal_card(self.player_sum, self.usable_ace)
            if self.player_sum > 21:
                self.round_done = True


        else:  # "stay" action == 0
            self.round_done = True


        if self.round_done:
            while self.dealer_sum < 17:
                self._deal_card(self.dealer_sum, False)


        # done
        reward = self._get_reward()
        self.round_done = True if reward != 0 else self.round_done


        # Return the updated observation, reward, and done flag
        return self._get_observation(), reward, self.round_done, {}


    def render(self, mode='human'):
        # Implement the logic for rendering the current state of the environment
        # ...
        print('filler')


    def _create_deck(self):

        print('generating new deck')
        # Create a new deck of cards (in this case, a standard deck with 4 sets of cards)
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        np.random.shuffle(deck)
        return deck


    def _deal_initial_cards(self):
        # initial cards -- one to dealer, two to player
        player_sum = self._get_card() + self._get_card()
        dealer_sum = self._get_card()
        usable_ace = 1 if 11 in [player_sum, dealer_sum] else 0


        return player_sum, dealer_sum, usable_ace


    def _deal_card(self, sum_value, usable_ace):
        # get new card
        card = self._get_card()
        sum_value += card
        if sum_value > 21 and usable_ace:
            sum_value -= 10
            usable_ace = 0
        return sum_value, usable_ace


    
    def _get_card(self):
        # draw card
        if len(self.deck) == 0:
            print('empty deck in _get_card()')
            self.deck = self._create_deck()
        card = self.deck.pop(0)
        return card


    def _get_observation(self):
        # Return the current observation (player_sum, dealer_sum, usable_ace)
        return self.player_sum, self.dealer_sum, self.usable_ace


    def _get_reward(self):
        if self.player_sum > 21:
            return -1  # player bust


        if self.dealer_sum > 21:
            return 1  # dealer bust


        if self.round_done:
            if self.player_sum > self.dealer_sum:
                return 1  # player win
            elif self.player_sum < self.dealer_sum:
                return -1  # player loss
            else:
                return 0  # same num


        return 0  # continue
