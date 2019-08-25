import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import math

class ExampleClass:
    """An example docstring for a class definition."""

    def __init__(self, name):
        """
        Blah blah blah.
        Parameters
        ---------
        name
            A string to assign to the `name` instance attribute.
        """
        self.name = name

def plot_categorical(df, size_inches=(5, 7)):
    """Plot counts of categorical features
    Args:
        df (dataframe): dataframe containing data to be ploted
        size_inches (tuple): plot size in inches
        num_cols: number of columns in plot
    Returns:
        fig, ax: plot
    """
    fig, ax = plt.subplots()
    fig.set_size_inches(size_inches)
    for i, column in enumerate(df.select_dtypes(include=['O'])):
        plt.subplot(1, 1, i + 1)
        df[column].value_counts().plot.barh()
        plt.title(column)
    return fig, ax
    

def plot_numerical(df, size_inches=(15, 20), num_cols = 5):
    """Plot histograms of categorical features
    Args:
        df (dataframe): dataframe containing data to be ploted
        size_inches (tuple): plot size in inches
        num_cols: number of columns in plot
    Returns:
        fig, ax: plot
    """
    num_features = df.select_dtypes(include=['float64']).shape[1]
    num_rows = math.ceil(num_features / num_cols)
    fig, ax = plt.subplots()
    fig.set_size_inches(size_inches)
    for i, column in enumerate(df.select_dtypes(include=['float64'])):
        plt.subplot(num_rows, num_cols, i + 1)        
        plt.hist(df.loc[df['diagnosis'] == 'M',column], alpha = 0.5, label = 'M')
        plt.hist(df.loc[df['diagnosis'] == 'B',column], alpha = 0.5, label = 'B')
        plt.title(column)
        plt.legend()
    return fig, ax
    