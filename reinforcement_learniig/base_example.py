
from dataset import Dataset

import gymnasium as gym
import gym_anytrading
from stable_baselines3.ppo.policies import MlpPolicy
from stable_baselines3 import A2C, PPO, DQN
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# import quantstats

# Импортируем данные о свечах с биржи, формируем датафрейм
data_binance = Dataset().get_data(days=90, symbol='BTCUSDT', tf='5m')
df = data_binance.copy()[['Open', 'High', 'Low', 'Close', 'Volume']]

window_size = 50  # количество предыдущих свечей для анализа
start_index = window_size
end_index = len(df)

#  Создаём окружение
def create_env(df, start_index, end_index, window_size):
    env = gym.make('forex-v0', df=df, frame_bound=(start_index, end_index), window_size=window_size)
    env.trade_fee = 0.0  # комиссия за сделку
    return env
# !!!
def env_maker():
    return create_env(df, start_index, end_index, window_size)


# Создаём модель агента
env = make_vec_env(lambda: env_maker(), n_envs=100)  # 1000
# model = PPO(MlpPolicy, env, verbose=1)
model = A2C(MlpPolicy, env, verbose=1)

# Случайная эволюция перед тренировкой
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)
print(f"среднее награда:{mean_reward:.2f} +/- {std_reward:.2f}")
# средняя награда:0.00 +/- 0.00

model.learn(total_timesteps=10_000_000)







