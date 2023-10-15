import numpy as np
import math

# Function to calculate the option payoff based on option type
def calculate_option_payoff(option_type, stock_price, strike_price):
    if option_type == "Call":
        return max(stock_price - strike_price, 0)
    elif option_type == "Put":
        return max(strike_price - stock_price, 0)

# Function to perform Monte Carlo simulation for option pricing and visualize results
def monte_carlo_option_pricing(option_type, stock_price, strike_price, volatility, risk_free_rate, time_to_maturity, num_simulations):
    dt = time_to_maturity / 252  # Assuming 252 trading days in a year
    option_payoffs = []
    price_paths = []

    for _ in range(num_simulations):
        price_path = []
        stock_price_copy = stock_price

        for _ in range(int(252 * time_to_maturity)):
            drift = (risk_free_rate - 0.5 * volatility**2) * dt
            shock = volatility * math.sqrt(dt) * np.random.normal(0, 1)
            stock_price_copy *= math.exp(drift + shock)
            price_path.append(stock_price_copy)

        price_paths.append(price_path)
        option_payoff = calculate_option_payoff(option_type, stock_price_copy, strike_price)
        option_payoffs.append(option_payoff)

    option_price = np.exp(-risk_free_rate * time_to_maturity) * np.mean(option_payoffs)
    return option_price, price_paths



