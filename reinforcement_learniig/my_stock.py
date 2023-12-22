
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
print(df)

