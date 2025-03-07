class Bot():
    def __init__(self, rFactor, min, max, cash, seat, hands):
        self.rFactor = rFactor
        self.min = min
        self.max = max
        self.cash = cash
        self.seat = seat
        self.handsPlayed = hands
    
    def bet(self):
        betAmt = self.min
        self.cash -= betAmt
        return betAmt
    def stats(self):
        print("Cash: {self.cash}, rFactor: {self.rFactor}, ")