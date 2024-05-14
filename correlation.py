"""Helper module to operate on correlation matrix DataFrames."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import seaborn as sns


def corr_triangle(corr: pd.DataFrame):
    """Format a correlation matrix to a triangular form, masking duplicate pairs as NA."""
    # implementation from Pandas Cookbook:
    #     https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#correlation
    mask = np.tril(np.ones_like(corr, dtype=np.bool_), k=-1)
    return corr.where(mask)


def corr_heatmap(corr: pd.DataFrame, title: str | None = None, cmap="coolwarm"):
    """Plot a correlation heatmap using Seaborn."""
    ax: Axes = plt.axes()
    sns.heatmap(corr, ax=ax, vmin=-1, vmax=1, cmap=cmap, annot=True)
    if title is not None:
        ax.set_title(title)
    plt.show()


def corr_style_heatmap(corr: pd.DataFrame, cmap="coolwarm"):
    """Configure & return a Styler to format a correlation matrix as a heatmap."""
    return (
        corr.style.background_gradient(cmap=cmap, axis=None, vmin=-1, vmax=1)
        .highlight_null("#f1f1f1")
        .format(precision=2)
    )
