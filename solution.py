import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 237396692 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    from scipy.stats import chi2
    alpha = 1 - p
    loc = (2 * x / 41**2).mean()
    scale = np.sqrt(np.var(2 * x / 41**2)) / np.sqrt(len(x))
    return 2 * len(x) * loc / chi2.ppf((1 - alpha) / 2, 2*len(x)), \
           2 * len(x) * loc / chi2.ppf((1 + alpha) / 2, 2*len(x))
