"""
Shared matplotlib/seaborn plot configuration.
"""

import matplotlib.pyplot as plt
import matplotlib as mpl


def set_style():
    mpl.rcParams.update({
        "figure.figsize": (12, 6),
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.3,
        "font.size": 12,
    })


def save_fig(fig, path: str, dpi: int = 150):
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    print(f"Saved: {path}")
