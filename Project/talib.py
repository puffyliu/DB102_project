import pandas as pd
import numpy as np
import talib as ta

close = np.array(bars.close)
print(ta.RSI(close))