"""
Shared utility functions across all analysis projects.
"""

import pandas as pd
import numpy as np


def load_csv(path: str, **kwargs) -> pd.DataFrame:
    df = pd.read_csv(path, **kwargs)
    print(f"Loaded: {df.shape[0]:,} rows x {df.shape[1]} cols")
    return df


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    missing = df.isnull().sum()
    pct = (missing / len(df) * 100).round(2)
    return pd.DataFrame({"missing": missing, "pct": pct}).query("missing > 0").sort_values("pct", ascending=False)


def describe_numeric(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include=np.number).describe().T.round(3)
