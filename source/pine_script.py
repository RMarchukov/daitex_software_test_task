from ta import momentum, trend
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


src = pd.Series([10, 20, 40, 60, 90, 200, 1000, 2, 5, 9, 21, 34, 55, 65, 567, 100, 2312, 32423, 2314])
ob = 70
os = 30
length = 14

rsi = momentum.RSIIndicator(close=src, window=length).rsi()
print(rsi.values)
max_list = []
min_list = []
for i in rsi:
    if i > 70:
        max_list.append(i)
    # auc = trend.EMAIndicator(pd.Series(max_list))
    elif i < 30:
        min_list.append(i)
    adc = trend.EMAIndicator(pd.Series(max_list))


plt.plot(rsi, label="RSI", color="blue", linewidth=2)
plt.axhline(70, color="red", linestyle="--", label="Overbought (70)")
plt.axhline(30, color="green", linestyle="--", label="Oversold (30)")
plt.legend()
plt.title("RSI Indicator")
plt.show()
