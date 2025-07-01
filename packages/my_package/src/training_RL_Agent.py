import os
os.environ["PYGLET_HEADLESS"] = "1"
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1024, 768))
display.start()

import gym
import gym_duckietown
import numpy as np
from stable_baselines3 import PPO
import torch
torch.cuda.empty_cache()

map_names = [
    'Duckietown-small_loop-v0',
    'Duckietown-4way-v0',
    'Duckietown-straight_road-v0',
    'Duckietown-udem1-v0',
    'Duckietown-4way_bordered-v0'
]

class MultiMapEnv(gym.Wrapper):
    def __init__(self, map_names):
        self.map_names = map_names
        env = gym.make(map_names[0])  # 不要传 enable_render
        super().__init__(env)

    def reset(self, **kwargs):
        map_name = np.random.choice(self.map_names)
        self.env = gym.make(map_name)
        return self.env.reset(**kwargs)


env = MultiMapEnv(map_names)
model = PPO('CnnPolicy', env, verbose=1, n_steps=64, batch_size=16)
model.learn(total_timesteps=100_000)
model.save('ppo_duckietown_multimap')
