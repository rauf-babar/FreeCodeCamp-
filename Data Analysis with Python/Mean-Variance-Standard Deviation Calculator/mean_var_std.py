import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    npArr = np.array(lst).reshape(3, 3)

    calculations = {
        "mean": [
            npArr.mean(axis=0).tolist(),   
            npArr.mean(axis=1).tolist(),   
            npArr.mean().tolist()          
        ],
        "variance": [
            npArr.var(axis=0).tolist(),
            npArr.var(axis=1).tolist(),
            npArr.var().tolist()
        ],
        "standard deviation": [
            npArr.std(axis=0).tolist(),
            npArr.std(axis=1).tolist(),
            npArr.std().tolist()
        ],
        "max": [
            npArr.max(axis=0).tolist(),
            npArr.max(axis=1).tolist(),
            npArr.max().tolist()
        ],
        "min": [
            npArr.min(axis=0).tolist(),
            npArr.min(axis=1).tolist(),
            npArr.min().tolist()
        ],
        "sum": [
            npArr.sum(axis=0).tolist(),
            npArr.sum(axis=1).tolist(),
            npArr.sum().tolist()
        ]
    }

    return calculations
