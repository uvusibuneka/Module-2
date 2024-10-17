import pandas as pd
import numpy as np 
import random as rnd
from typing import *
from linear_model import *
import metrics

path = '/home/uvusibuneka/Desktop/СИИ/california_housing_train.csv' 
df = pd.read_csv(path)

df = (df - df.min())/(df.max() - df.min())
df = df.dropna()

df = df.reset_index(drop=True)
df["ones"] = np.ones(len(df))

model = linear_model(df, metrics.MSE())
model.split_df("median_house_value")
model.fit(300, lr=0.00001)
print(model.coef_determination())
print(model.weights)