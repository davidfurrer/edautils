#%%
import edautils
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

#%%
df = pd.read_csv('data/data-breast-cancer.csv')

#%%
edautils.plot_numerical(df)

#%%
edautils.plot_categor(df)

