import pandas as pd
import numpy as np

np.random.seed(123)
N = 10000
portfolio = pd.DataFrame({
    "EAD": np.random.lognormal(mean=10, sigma=1, size=N),
    "PD": np.random.uniform(0.01, 0.20, size=N),
    "LGD": np.random.uniform(0.2, 0.6, size=N),
})
portfolio.to_csv("portfolio_data.csv", index=False)