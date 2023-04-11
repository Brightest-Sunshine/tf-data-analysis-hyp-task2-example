import pandas as pd
import numpy as np
from hyppo.ksample import MMD


chat_id = 453878141 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, pvalue = MMD(compute_kernel="laplacian", gamma=1).test(x, y)
    alpha = 0.05 
    if pvalue < alpha:
        return True
    else:
        return False
