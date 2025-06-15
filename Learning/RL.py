import gym
import random
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

env = gym.make('FrozenLake-v1',desc=['HSFFG'],is_slippery=False)

Q = np.zeros([env.observation_space.n, env.action_space.n])

def policy(qs,e=0):
  if e > random.random():
    return random.choice([0,2])
  else:
    if qs[0] > qs[2]: return 0
    elif qs[0] < qs[2]: return 2
    else: return random.choice([0,2])

num_episodes = 100
discount = 0.9
Q = Q*0.0
for i in range(num_episodes):
  state, _ = env.reset()
  done = False
  while not done:
    action = policy(Q[state, :],e=0.1)
    new, reward, done, _ = env.step(action)
    Q[state,action] = reward + discount*np.max(Q[new, :])
    state = new

print(Q[1:-1,[0,2]])