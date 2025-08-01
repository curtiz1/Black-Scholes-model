# -*- coding: utf-8 -*-
"""BlackScholes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n3FS31E6Y4-Avc7oJDGoDpuGX27AXryg
"""





from numpy import exp, sqrt, log
from scipy.stats import norm

class BlackScholes:
    def __init__(
        self,
        time_to_maturity: float,
        strike: float,
        current_price: float,
        volatility: float,
        interest_rate: float,
    ):
        self.time_to_maturity = time_to_maturity
        self.strike = strike
        self.current_price = current_price
        self.volatility = volatility
        self.interest_rate = interest_rate

