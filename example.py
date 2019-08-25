#%%
import edautils
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

#cancer example
#%%
df = pd.read_csv('data/data-breast-cancer.csv')
df2 = pd.read_csv('data/mpg.csv')
#%%
fig, ax = edautils.plot_numerical(df, num_cols = 5)
fig.savefig("png/numerical_example1.png", dpi=150)
plt.close(fig) 

#%%
fig, ax = edautils.plot_numerical(df, num_cols = 5, target_col = 'diagnosis')
fig.savefig("png/numerical_example2.png", dpi=150)
plt.close(fig) 

#%%
fig, ax = edautils.plot_categorical(df, num_cols = 1)
fig.savefig("png/categorical_example1.png", dpi=150)
plt.close(fig) 

#mpg example
#%%
fig, ax = edautils.plot_numerical(df2, num_cols = 5)
fig.savefig("png/numerical_example1.2.png", dpi=150)
plt.close(fig) 


#%%
fig, ax = edautils.plot_categorical(df2, num_cols = 3, size_inches=(30, 10))
fig.savefig("png/categorical_example1.2.png", dpi=150)
plt.close(fig) 

edautils.summary_report(df)
