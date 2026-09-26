import math
import sys
print(sys.executable)
#import numpy as np
def binomial_option_price(S0, K, r, u, d, t, option_type):

    #Risk-free prob measure
    qu = ((1+r)-d)/(u-d)
    qd = 1 - qu

    #Building the possible values of underlying at maturity
    S_T = []
    for i in range(t + 1):
        S = S0 * (u**i) * (d**(t-i))
        S_T.append(S)
    #print(S_T)

    #Building the payoff vector for a European Call Option
    payoffs = []
    for S in S_T:
        if option_type == "call":
            payoff = max(S-K, 0)
        elif option_type == "put":
            payoff = max(K-S, 0)
        payoffs.append(payoff)
    #print(payoffs)

    #Pricing the derivative
    #Initialize it as the payoff

    option_values = payoffs
    for step in range(t):
        new_values = []
        for i in range(len(option_values)-1):
            value = (qu * option_values[i+1] + qd * option_values[i])/(1+r)
            new_values.append(value)
        option_values = new_values
    
    return option_values[0]
s = binomial_option_price(100, 80, 0.05, 1.2, 0.8, 3, "put")
print(s)