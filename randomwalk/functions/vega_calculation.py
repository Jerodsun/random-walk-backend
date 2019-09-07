import numpy as np
import scipy.stats as si

def vega_div(S, K, T, r, q, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    #q: continuous dividend rate
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    vega = 1 / np.sqrt(2 * np.pi) * S * np.exp(-q * T) * np.exp(-(d1 ** 2) * 0.5) * np.sqrt(T)
    
    return vega


def vega(S, K, T, r, sigma):

    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    vega = S * si.norm.cdf(d1, 0.0, 1.0) * np.sqrt(T)
    
    return vega