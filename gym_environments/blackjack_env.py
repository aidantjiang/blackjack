import gym
from gym import spaces
import numpy as np

class BlackjackEnv(gym.Env):
    def __init__(self):
        super(BlackjackEnv, self).__init__()

        # print('initializing')

        self.action_space = spaces.Discrete(2)  # 0 for "stay" and 1 for "hit"
        self.observation_space = spaces.Tuple((
            spaces.Discrete(34),  # current sum range 0-32
            spaces.Discrete(34),  # dealer sum range 0-32
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
        # print('resetting')
        self.deck = self._create_deck()
        self.player_sum, self.dealer_sum, self.usable_ace = self._deal_initial_cards()
        self.round_done = False


        # initial observation
        # print('initial sums')
        # print('player sum initial', self.player_sum)
        # print('dealer sum initial', self.dealer_sum)
        return self._get_observation()


    def step(self, action):
        # import pdb; pdb.set_trace()
        assert self.action_space.contains(action), "Invalid action"
        # print('stepping')

        # print('player sum before hit/stay', self.player_sum)
        # print('dealer sum before hit/stay', self.dealer_sum)
        if action == 1:  # "hit"
            # print('hit')
            new_val = self._get_card()
            # print('player dealt card', new_val)
            self.player_sum += new_val;
            if self.player_sum > 21 and self.usable_ace:
                # print('used ace')
                self.player_sum -= 10
                self.usable_ace = 0
            if self.player_sum > 21:
                self.round_done = True


        else:  # "stay" action == 0
            # print('stay')
            self.round_done = True


        if self.round_done:
            # print ('round finished')
            # print('initial dealer sum', self.dealer_sum)
            while self.dealer_sum < 17:
                new_val = self._get_card()
                # dealer's ace is always 11
                # print('dealer dealt card', new_val)
                self.dealer_sum += new_val
                # print('updated dealer sum', self.dealer_sum)

        # print('player sum after hit/stay', self.player_sum)
        # print('dealer sum after hit/stay', self.dealer_sum)
        # done
        reward = self._get_reward()
        self.round_done = True if reward != 0 else self.round_done


        # Return the updated observation, reward, and done flag
        return self._get_observation(), reward, self.round_done, {}


    def render(self, mode='human'):
        # Implement the logic for rendering the current state of the environment
        # ...
        print('RESULTS: \n')
        print('player: ', self.player_sum)
        print('dealer: ', self.dealer_sum, '\n')


    def _create_deck(self):

        # print('generating new deck')
        # Create a new deck of cards (in this case, a standard deck with 4 sets of cards)
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        np.random.shuffle(deck)
        return deck


    def _deal_initial_cards(self):
        # initial cards -- one to dealer, two to player
        # print("dealing initial cards")
        player_sum = self._get_card() + self._get_card()
        dealer_sum = self._get_card()
        usable_ace = 1 if 11 in [player_sum, dealer_sum] else 0


        return player_sum, dealer_sum, usable_ace

    # THE ERROR IS HERE BUT NOT ANYMORE!
    def _deal_card(self, sum_value, usable_ace):
        # get new card
        card = self._get_card()
        # sum_value += card
        # return sum_value, usable_ace
        return card, usable_ace


    
    def _get_card(self):
        # draw card
        # import pdb; pdb.set_trace()
        if len(self.deck) == 0:
            # print('empty deck in _get_card()')
            self.deck = self._create_deck()
        card = self.deck.pop(0)
        return card


    def _get_observation(self):
        # print('retuning oberservation')
        # RETURNS WHAT IS PASSED INTO Q TABLE
        # Return the current observation (player_sum, dealer_sum, usable_ace)
        return self.player_sum, self.dealer_sum, self.usable_ace


    def _get_reward(self):
        # print ('getting rewards')
        if self.player_sum > 21:
            # print('player bust')
            # print(' \n\n\n\nplayer loss\n\n\n\n')
            return -10  # player bust


        if self.dealer_sum > 21:
            # print('dealer bust')
            # print(' \n\n\n\nplayer win\n\n\n\n')
            return 1  # dealer bust


        if self.round_done:
            if self.player_sum > self.dealer_sum:
                # print(' \n\n\n\nplayer win\n\n\n\n')
                return 10  # player win
            elif self.player_sum < self.dealer_sum:
                # print(' \n\n\n\nplayer loss\n\n\n\n')
                return -10  # player loss
            else:
                # print(' \n\n\n\ntie\n\n\n\n')
                return -1  # same num


        return -1  # continue
