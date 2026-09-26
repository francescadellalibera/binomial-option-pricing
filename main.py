import math

from bynomial_model import binomial_option_price
from replicating_ptf import replication 

#Example to show that in no-arbitrage the price of a replicating portfolio is the same as the price of the option

S0 = 100;
K = 80;
r = 0.05;
u = 1.2;
d = 0.8;
t = 3;
option_type = "put";

#Option price
p = binomial_option_price(S0, K, r, u, d, t, option_type)
print(f"Option price: {p: .4f}")

#Delta and B
(d,b) = replication(S0, K, r, u, d, t, option_type)
print(f"Delta: {d: .4f}")
print(f"Risk-less asset: {b: .4f}")

#Value at t = 0 of the replicating ptf
v = d*S0 + b
print(f"Price of the replicating portfolio: {v: .4f}")

if abs(p- v)>1e-10:
        raise ValueError("Arbitrage opportunity detected")
