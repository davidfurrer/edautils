#%%
import edautils
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

#%%
df = pd.read_csv('data/data-breast-cancer.csv')

#%%
fig, ax = edautils.plot_numerical(df)
fig.savefig("png/numerical_example1.png", dpi=150)
plt.close(fig) 


#%%
fig, ax = edautils.plot_categorical(df)
fig.savefig("png/categorical_example1.png", dpi=150)
plt.close(fig) 
