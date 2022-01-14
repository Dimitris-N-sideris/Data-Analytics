import numpy as np


def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    data = np.array([list[0:3], list[3:6], list[6:9]])

    calculations = {
        "mean": [data.mean(axis=0).tolist(), data.mean(axis=1).tolist(), data.mean()],
        "variance": [data.var(axis=0).tolist(), data.var(axis=1).tolist(), data.var()],
        "standard deviation": [
            data.std(axis=0).tolist(),
            data.std(axis=1).tolist(),
            data.std(),
        ],
        "max": [data.max(axis=0).tolist(), data.max(axis=1).tolist(), data.max()],
        "min": [data.min(axis=0).tolist(), data.min(axis=1).tolist(), data.min()],
        "sum": [data.sum(axis=0).tolist(), data.sum(axis=1).tolist(), data.sum()],
    }

    return calculations
