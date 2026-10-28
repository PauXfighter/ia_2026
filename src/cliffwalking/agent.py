import numpy as np
import random

from iaLib import agent

class Agent(agent.Agent):
    def __init__(self, alpha, gamma, seed=0):
        super().__init__(long_memoria=0)

        self.__alpha = alpha
        self.__gamma = gamma
        self.q = None

        np.random.seed(seed)
        random.seed(seed)


    def epsilon_greedy(self, eps):
        """ Selects an action using the epsilon-greedy policy.

        TODO

        Returns:

        """
        pass

    def train(self, env, n_estats, n_accions, episodes, eps=0.1):
        """ Trains the agent using the SARSA algorithm.

        TODO

        Returns:

        """
        self.q = np.zeros((n_estats, n_accions))
        for _ in tqdm(range(1, episodes + 1)):
            s, _ = env.reset()

            #TODO


    def actua(self, estat):
        """ Selects an action for the given state.

        TODO

        Args:
            estat:

        Returns:

        """
        pass

