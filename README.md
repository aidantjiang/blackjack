## installations:

pip install gym
pip install numpy
pip install matplotlib

## how blackjack works

CARD VALUES

- aces: 1 or 11
- all number cards: their values
- royalty: 10

RULES

- your goal is to beat the dealer and be as close to 21 as possible while not going over
- you win if: the dealer "busts" or you are closer to 21 then the dealer is
- you lose if: you "bust" or the dealer is closer to 21 than you are
- the dealer must: "stay" (as opposed to "hit", or get another card) if they are >= 17 in term of card value

this implements a q-learning algorithmic approach to train an agent into learning how to play blackjack using reinforcement learning
