import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

def plot_categorical(df):
    fig, ax = plt.subplots()
    fig.set_size_inches((5, 7))
    for i, column in enumerate(df.select_dtypes(include=['O'])):
        plt.subplot(1, 1, i + 1)
        df[column].value_counts().plot.barh()
        plt.title(column)
    return fig, ax
    

def plot_numerical(df):
    #NUM_FEATURES = df.select_dtypes(include=['float64']).shape[1]

    fig, ax = plt.subplots()
    fig.set_size_inches((15, 20))
    for i, column in enumerate(df.select_dtypes(include=['float64'])):
        plt.subplot(6, 6, i + 1)        
        plt.hist(df.loc[df['diagnosis'] == 'M',column], alpha = 0.5, label = 'M')
        plt.hist(df.loc[df['diagnosis'] == 'B',column], alpha = 0.5, label = 'B')
        plt.title(column)
        plt.legend()
    return fig, ax
    