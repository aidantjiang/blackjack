## installations:

pip install gym
pip install numpy
pip install matplotlib

to install all needed pip packages, run `pip install -r requirements.txt`

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

ERROR FIXING

- to be safe, when first initializing this project, run `export PYTHONPATH='.'` after you've cd'ed into the blackjack folder
- then, to simulate the reinforcement learning agent, run `python3 agents/rl_agent.py`
- to run the pygame, run `python3 main.py`
