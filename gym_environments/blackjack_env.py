import gym
from gym import spaces
import numpy as np
import time
from visualization.game import deck
# from visualization.deck import Deck

# deck = Deck()

class BlackjackEnv(gym.Env):
    def __init__(self):
        super(BlackjackEnv, self).__init__()

        # print('initializing')

        self.action_space = spaces.Discrete(2)  # 0 for "stay" and 1 for "hit"
        self.observation_space = spaces.Tuple((
            spaces.Discrete(34),  # current sum range 0-32
            spaces.Discrete(34),  # dealer sum range 0-32
            spaces.Discrete(5)    # ace # you COULD be dealt 4 aces
        )) # TODO: spaces should be Discrete(32), Discrete(32), Discrete(2)

        self.player_sum = None
        self.dealer_sum = None
        self.usable_ace = None
        self.round_done = None

        self.cards = None

        # initialize envrion
        self.reset()
    def reset(self):
        deck._create_deck()
        surfaces, self.player_sum, self.dealer_sum, self.usable_ace = deck._deal_initial_cards()
        self.round_done = False

        self.cards = [surfaces[0], surfaces[1]]

        return self._get_observation()


    def step(self, action, game=False):
        # import pdb; pdb.set_trace()
        assert self.action_space.contains(action), "Invalid action"
        # print('stepping')

        # print('player sum before hit/stay', self.player_sum)
        # print('dealer sum before hit/stay', self.dealer_sum)
        if action == 1:  # "hit"
            # print('hit')
            new_val, surface = deck._get_card()
            self.cards.append(surface)
            if new_val == 11:
                self.usable_ace += 1
            # print('player dealt card', new_val)
            self.player_sum += new_val;
            if self.player_sum > 21 and self.usable_ace:
                # print('used ace')
                self.player_sum -= 10
                self.usable_ace -= 1
            if self.player_sum > 21:
                self.round_done = True


        else:  # "stay" action == 0
            # print('stay')
            self.round_done = True


        if self.round_done:
            # print ('round finished')
            # print('initial dealer sum', self.dealer_sum)
            while self.dealer_sum < 17:
                new_val, _ = deck._get_card()
                # dealer's ace is always 11
                # print('dealer dealt card', new_val)
                self.dealer_sum += new_val
                # print('updated dealer sum', self.dealer_sum)

        # print('player sum after hit/stay', self.player_sum)
        # print('dealer sum after hit/stay', self.dealer_sum)
        # done
        reward = self._get_reward()
        self.round_done = True if reward != 0 else self.round_done

        # pause in game
        if (game):
            time.sleep(0.6)


        # Return the updated observation, reward, and done flag
        return self._get_observation(), reward, self.round_done, {}


    def render(self, mode='human'):
        # Implement the logic for rendering the current state of the environment
        # ...
        num = self._get_reward()
        print('agent', self.player_sum)
        print('dealer', self.dealer_sum)
        if num == 10 or num == 100:
            print('win\n')
        else:
            print('lose/draw\n')

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
            return -100  # player bust


        if self.dealer_sum > 21:
            # print('dealer bust')
            # print(' \n\n\n\nplayer win\n\n\n\n')
            return 10  # dealer bust


        if self.round_done:
            if self.player_sum > self.dealer_sum:
                # print(' \n\n\n\nplayer win\n\n\n\n')
                return 100  # player win
            elif self.player_sum < self.dealer_sum:
                # print(' \n\n\n\nplayer loss\n\n\n\n')
                return -100  # player loss
            else:
                # print(' \n\n\n\ntie\n\n\n\n')
                return 0 # same num


        return 0  # continue
