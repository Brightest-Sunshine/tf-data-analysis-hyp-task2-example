import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 453878141 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    samples = [x, y]
    result = anderson_ksamp(samples)
    alpha = 0.05
    if result.statistic < result.critical_values[2]:
        return False
    else:
        return True
