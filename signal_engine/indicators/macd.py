import pandas as pd

def macd(price: pd.Series):
    fast = price.ewm(span=12, adjust=False).mean()
    slow = price.ewm(span=26, adjust=False).mean()
    hist = fast - slow
    signal = hist.ewm(span=9, adjust=False).mean()
    return hist, signal
