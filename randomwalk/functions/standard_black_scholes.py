import numpy as np
import scipy.stats as si

def vanilla_call(S, K, T, r, sigma):
    # S: Spot Price
    # K: Strike Price
    # T: Time to maturity
    # r: interest rate
    # sigma: volatility

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T ) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    
    return call

def vanilla_put(S, K, T, r, sigma):
    # S: Spot Price
    # K: Strike Price
    # T: Time to maturity
    # r: interest rate
    # sigma: volatility

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T ) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0)) - S * si.norm.cdf(-d1, 0.0, 1.0))

    return put


def call_div(S, K, T, r, q, sigma):
    
    # S: Spot Price
    # K: Strike Price
    # T: Time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset 
    # sigma: volatility
    
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    call = (S * np.exp(-q * T) * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    
    return call


def put_div(S, K, T, r, q, sigma):
    
    # S: Spot Price
    # K: Strike Price
    # T: Time to maturity
    # r: interest rate
    # q: rate of continuous dividend paying asset 
    # sigma: volatility
    
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - q - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * np.exp(-q * T) * si.norm.cdf(-d1, 0.0, 1.0))
    
    return put