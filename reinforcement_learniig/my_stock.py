
video = 'https://www.youtube.com/watch?v=d3a_Fs753-A'
cod = 'https://colab.research.google.com/drive/18OVthjc_dunpLtBgWbCIqWLzE4LoA0_c?usp=sharing#scrollTo=krmvJpHp8Y1O'


from dataset import Dataset
import gymnasium as gym
import gym_anytrading

from stable_baselines3.common.vec_env import DummyVecEnv  #pip install stable-baselines3[extra]
from stable_baselines3 import A2C, PPO

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# Импортируем данные о свечах с биржи, формируем датафрейм и записываем в файл
# data = Dataset().get_data(days=90, symbol='BTCUSDT', tf='5m')
# data.to_csv('data_BTCUSDT_90d_5m')
df = pd.read_csv('data_BTCUSDT_90d_5m').set_index('Date')
# df = df[-1000:]
#Инициализируем среду, устанавливая размер окна и данные обучения
window_size = 10
end_index_data = int(len(df) * 0.8)

env_maker = lambda: gym.make('stocks-v0', df=df, frame_bound=(window_size, end_index_data), window_size=window_size)
env = DummyVecEnv([env_maker])

model = A2C('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=100_000)

env = gym.make('stocks-v0', df=df, frame_bound=(len(df) - end_index_data, len(df)), window_size=window_size)
obs, info = env.reset()


while True:
    # action = env.action_space.sample()
    obs = obs[np.newaxis, ...]
    action, _states = model.predict(observation=obs)
    obs, reward, profit, done, info = env.step(action=action)
    if done:
        print('info', info)
        break
plt.figure(figsize=(15, 6), facecolor='w')
plt.cla()
env.unwrapped.render_all()
plt.show()
