import math

def replication(S0, K, r, u, d, t, option_type):
    #Computing the replicating portfolio of a European put or call option
    #At each t, V_t = DeltaS_t + B
    #We define Delta = Vu - Vd/Su - Sd, "how much the option price is affected by the variation of its underlying"

    #Risk-neutral probabilities
    qu = ((1+r)-d)/((u-d))
    qd = 1 - qu

    #Stock-prices after the first step
    S_u = S0*u
    S_d = S0*d

    # Option values at maturity
    option_values = []

    for i in range(t + 1):

        S = S0 * (u ** i) * (d ** (t - i))

        if option_type == "call":
            payoff = max(S - K, 0)

        elif option_type == "put":
            payoff = max(K - S, 0)

        else:
            raise ValueError("option_type must be 'call' or 'put'.")

        option_values.append(payoff)

     # Backward induction until the first step, same idea as option pricing
    for step in range(t - 1):

        new_values = []

        for i in range(len(option_values) - 1):

            value = (
                qu * option_values[i + 1]
                + qd * option_values[i]
            ) / (1 + r)

            new_values.append(value)

        option_values = new_values

    # Option values after the first step
    V_u = option_values[1]
    V_d = option_values[0]

    # Delta
    delta = (V_u - V_d) / (S_u - S_d)

    # Risk-free position
    B = (V_d - delta * S_d) / (1 + r)

    # The value of the portfolio, that under NA coincides with the price of the option, is given by
    # delta * S0 + B
    return delta, B

