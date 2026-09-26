# binomial-option-pricing
Discrete-time multiperiod binomial model for European option pricing
The first code defines a function which returns the price of any call or put European option, in a time-discrete framework, given the initial value of the underlying, the strike price, the riskless interest rate, the up and down factors, the number of periods (assuming years), and the option type.
The second code defines a function which, given the same inputs as the other, gives back the Delta and B of the replicating portfolio. 
In the main, we compare the price of the option given by the first code, with the price at time 0 of the replicating portfolio. If these do not match, the code gives a warning: an arbitrage has been detected. 
