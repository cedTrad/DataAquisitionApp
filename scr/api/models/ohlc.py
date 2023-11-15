from dataclasses import dataclass

@dataclass
class OHLC:
    symbol : str
    strdate : float
    open : float
    high : float
    low : float
    close : float
    volume : float
    enddate : float
    