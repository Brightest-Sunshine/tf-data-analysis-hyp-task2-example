import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 453878141 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    statistic, critical_values, pvalue = anderson_ksamp([x, y])
    alpha = 0.05
    if statistic > critical_values[2]:
        return True
    else:
        return False
