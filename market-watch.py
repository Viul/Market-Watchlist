
class Watchlist:

    def __init__(self, stock, dividend, rate):
        self.stock = stock
        self.dividend = dividend
        self.rate = rate

    def stock_format(self):
        return ('{} {} {}'.format(self.stock, self.dividend, self.rate))
    

class Tech(Watchlist):
    def __init__(self, stock, dividend, rate, pe_ratio, beta):
        super().__init__(stock, dividend, rate)
        self.pe_ratio = pe_ratio
        self.beta = beta

    def tech_format(self):
        return ('{} {} {}'.format(self.stock, self.pe_ratio, self.beta))

stock1 = Watchlist('RYLD:', 1.13, 'Monthly')
stock2 = Watchlist('STAG:', 1.034, 'Monthly')

tech1 = Tech('MSI', 1.21, 'Quarterly',  36.51, 0.93)

print(tech1.tech_format())