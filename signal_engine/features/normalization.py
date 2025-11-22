import pandas as pd

def minmax(series: pd.Series):
    return (series - series.min()) / (series.max() - series.min())
