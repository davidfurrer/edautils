import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def plot_categorical(df, size_inches=(5, 7), num_cols=None):
    """Plot counts of categorical features
    Args:
        df (dataframe): dataframe containing data to be ploted
        size_inches (tuple): plot size in inches
        num_cols: number of columns in plot
    Returns:
        fig, ax: plot
    """
    num_features = df.select_dtypes(include=['O']).shape[1]
    num_rows = math.ceil(num_features / num_cols)
    fig, ax = plt.subplots()
    fig.set_size_inches(size_inches)
    for i, column in enumerate(df.select_dtypes(include=['O'])):
        plt.subplot(num_rows, num_cols, i + 1)
        df[column].value_counts().plot.barh()
        plt.title(column)
    return fig, ax


def plot_numerical(df, size_inches=(15, 20), num_cols=None, target_col=None):
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
        if target_col == None:
            plt.hist(df[column], alpha=0.5)
        else:
            target_cats = df[target_col].unique()
            for target_cat in target_cats:
                plt.hist(df.loc[df[f'{target_col}'] == f'{target_cat}',
                                column], alpha=0.5, label=f'{target_cat}')
            plt.legend()
        plt.title(column)

    return fig, ax


def summary_report(df):
    print(df.shape)
    print(f'Number of missing values: {df.isnull().sum().sum()}')
