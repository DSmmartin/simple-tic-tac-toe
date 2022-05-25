import numpy as np
import random


class IAPlayer:
    def __init__(self, state_space, action_space) -> None:
        self.__q_table = np.zeros((state_space, action_space))
        self.exploration_parameters = {
            "epsilon": 1.0,       # Exploration rate
            "max_epsilon": 1.0,   # Exploration probability at start
            "min_epsilon": 0.05,  # Minimum exploration probability
            "decay_rate": 0.005,  # Exponential decay rate for exploration prob
        }

    def epsilon_greedy_policy(self, state, action_sample):
        # Randomly generate a number between 0 and 1
        random_int = random.uniform(0, 1)
        # if random_int > greater than epsilon --> exploitation
        if random_int > self.exploration_parameters.get("epsilon"):
            # Take the action with the highest value given a state
            # np.argmax can be useful here
            return np.argmax(self.__q_table[state])
        # else --> exploration
        else:
            return action_sample

    def greedy_policy(self, state):
        # Exploitation: take the action with the highest state, action value
        return np.argmax(self.__q_table[state])
