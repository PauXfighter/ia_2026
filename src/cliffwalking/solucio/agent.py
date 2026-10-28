import random

import numpy as np
from iaLib import agent
from tqdm import tqdm


class AgentSARSA(agent.Agent):
    def __init__(self, alpha, gamma, seed=0):
        super().__init__(long_memoria=0)

        self.__alpha = alpha
        self.__gamma = gamma
        self.q = None

        np.random.seed(seed)
        random.seed(seed)


    def epsilon_greedy(self, action_space, state, eps=0.1):
        """Choose an action `a` in the current world state (s)."""
        if random.random() < eps:
            action = action_space.sample()
        else:
            best = np.flatnonzero(self.q[state] == self.q[state].max())
            action = np.random.choice(best)

        return action

    def train(self, env, n_estats, n_accions, episodes, eps=0.1):
        self.q = np.zeros((n_estats, n_accions))
        for _ in tqdm(range(1, episodes + 1)):
            s, _ = env.reset()
            a = self.epsilon_greedy(env.action_space, s, eps)
            done = False
            while not done:
                s2, r, done, _, _ = env.step(a)
                a2 = self.epsilon_greedy(env.action_space, s2, eps) if not done else None
                if not done:
                    self.q[s, a] += self.__alpha * (r + self.__gamma * self.q[s2, a2] - self.q[s, a])
                else:
                    self.q[s, a] += self.__alpha * (r - self.q[s, a])
                s, a = s2, a2 if a2 is not None else 0


    def actua(self, estat):
        if self.q is None:
            raise ValueError("Abans d'executar l'agent ha d'estar entrenat.")

        best = np.flatnonzero(self.q[estat] == self.q[estat].max())
        action = np.random.choice(best)

        return action

