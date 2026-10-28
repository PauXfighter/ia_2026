import gymnasium as gym
import numpy as np

from cliffwalking.agent import Agent


def print_policy(Q, n_states, goal, cliff, start):
    """ Print the policy derived from Q-values.

    Args:
        Q: Q-value table
        n_states: Integer number of states
        goal: Goal position (row, col)
        cliff: Set of cliff positions {(row, col), ...}
        start: Start position (row, col)

    """
    arrows = {0: '^', 1: '>', 2: 'v', 3: '<'}
    grid = [['' for _ in range(12)] for __ in range(4)]
    for idx in range(n_states):
        r, c = idx // 12, idx % 12
        if (r, c) == goal:
            grid[r][c] = 'G'
        elif (r, c) in cliff:
            grid[r][c] = 'C'
        elif (r, c) == start:
            grid[r][c] = 'S'
        else:
            a = np.argmax(Q[idx])
            grid[r][c] = arrows[a]
    for row in grid:
        print(' '.join(f'{cell:>2}' for cell in row))
    print()

def main():
    # Per entrenar l'agent posam sempre el render_mode a None
    env = gym.make(
        "CliffWalking-v1",
        render_mode=None,
    )
    n_estats = env.observation_space.n
    n_actions = env.action_space.n

    agent = Agent(alpha=0.5, gamma=1.0)

    # TODO

    # Per a visualitzar l'agent ja entrenat posam el render_mode a human
    env = gym.make(
        "CliffWalking-v1",
        render_mode="human",
    )

    done = False

    # AGENT RANDOM
    estat, _ = env.reset()
    print(estat)
    
    while not done:
        action = env.action_space.sample()
        estat, _, done, _, _ = env.step(action)


if __name__ == '__main__':
    main()