class Asset:
    def __init__(self, name, drift_rate, std_dev):
        self.name=name
        self.drift_rate=drift_rate
        self.std_dev=std_dev


class Option:
    def __init_(self, option_price_at_time, call_price, put_price, option_expiration, time_until_maturity, strike_price):
        self.option_price_at_time=option_price_at_time
        self.call_price=call_price
        self.put_price=put_price
        self.option_expiration=option_expiration
        self.time_until_maturity=time_until_maturity
        self.strike_price=strike_price

    def set_std_normal_cdf(x):
        self.std_normal_cdf = x
    def set_pdf(x):
        self.pdf = x
