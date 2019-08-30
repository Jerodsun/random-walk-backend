import numpy as np
import pandas as pd
import time

# mu=1
# n=50
# dt=0.1
# x0=100

def brownianMotion(sigma, mu, x0, n=50, dt=0.1, repeat=5):

    now = time.time()
    np.random.seed(int(str(hash(now))[-8:])) # last 8 integers, unique
    runs = {}
    for i in range(repeat):
        x=pd.DataFrame()        
        step=np.exp((mu-sigma**2/2)*dt)*np.exp(sigma*np.random.normal(0,np.sqrt(dt),(1,n)))
        x=pd.DataFrame(x0*step.cumprod())
        runs[i + 1] = x.iloc[:, 0] # temporary? hack to remove another json wrapper

    return runs, now

# Verified reproducibility with np.random.seed(1)

# https://en.wikipedia.org/wiki/Geometric_Brownian_motion