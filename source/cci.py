import pandas as pd
from ta.trend import CCIIndicator
from random import randint

li = []
while len(li) < 30:
    r = randint(-200, 200)
    li.append(r)

cci = CCIIndicator(high=pd.Series(120), low=pd.Series(-100), close=pd.Series(li), window=30)
