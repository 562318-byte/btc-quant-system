def volatility_filter(atr, price):
    # If ATR is too high relative to price → reduce trust
    ratio = atr / price
    return 1 - ratio.clip(upper=0.03)  # max 3% ATR filter
