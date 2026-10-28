import gymnasium as gym
import numpy as np

from cliffwalking.solucio.agent import AgentSARSA


def print_policy(Q, n_states, goal, cliff, start):
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
    env = gym.make(
        "CliffWalking-v1",
        render_mode=None,
    )
    n_estats = env.observation_space.n
    n_actions = env.action_space.n

    agent = AgentSARSA(alpha=0.5, gamma=1.0)
    agent.train(env, n_estats, n_actions, 2000)

    print_policy(agent.q, n_estats, (3, 11), {(3, c) for c in range(1, 11)}, (3, 0))

    env = gym.make(
        "CliffWalking-v1",
        render_mode="human",
    )
    initial_state, _ = env.reset()
    done = False

    s = initial_state
    while not done:
        action = agent.actua(s)
        s, _, done, _, _ = env.step(action)













if __name__ == '__main__':
    main()