# Q-LEARNING IN THIS AGENT

import gym
import numpy as np
import matplotlib.pyplot as plt

from gym_environments.blackjack_env import BlackjackEnv

class QLearningAgent:
    def __init__(self, env, learning_rate=0.1, discount_factor=0.9, epsilon=0.9, epsilon_decay=0.000005): # change epsilon back to ???;
        self.env = env
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.q_table = np.zeros((env.observation_space[0].n, env.observation_space[1].n, env.observation_space[2].n, env.action_space.n))


    def choose_action(self, observation):
        if np.random.uniform(0, 1) < self.epsilon:
            # Explore: choose a random action
            action = self.env.action_space.sample()
        else:
            # Exploit: choose the action with maximum Q-value for the given observation
            action = np.argmax(self.q_table[observation])
        return action


    def update_q_table(self, observation, action, reward, next_observation):
        current_q = self.q_table[observation][action]
        max_q = np.max(self.q_table[next_observation])
        new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (reward + self.discount_factor * max_q)
        self.q_table[observation][action] = new_q


    def train(self, num_episodes):
        episode_rewards = []
        avg_rewards = []
        total_reward = 0
        for episode in range(num_episodes):
            observation = self.env.reset()
            done = False
            total_reward = 0
            while not done:
                action = self.choose_action(observation)
                next_observation, reward, done, _ = self.env.step(action)
                self.update_q_table(observation, action, reward, next_observation)
                observation = next_observation
                total_reward += reward
            if (episode + 1) % 40000 == 0:
                episode_rewards.append(total_reward)
                avg_reward = total_reward / 40000  # Calculate average reward
                avg_rewards.append(avg_reward)
                print('Episode', episode + 1, 'completed')
                total_reward = 0
            self.epsilon -= self.epsilon_decay
            
#         x = range(40000, num_episodes + 1, 40000)
#         plt.plot(x, avg_rewards)
#         plt.xlabel('Episodes')
#         plt.ylabel('Average Reward')
#         plt.title('Q-learning Performance')
#         plt.show()