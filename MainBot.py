class Bot():
    def __init__(self, randomFactor, riskFactor, min, max, cash, seat, hands):
        self.riskFactor = riskFactor
        self.randomFactor = randomFactor
        self.min = min
        self.max = max
        self.cash = cash
        self.seat = seat
        self.handsPlayed = hands
        
    def newHand(self):
        pass
    def bet(self):
        betAmt = self.min
        self.cash -= betAmt
        return betAmt
    def stats(self):
        print("Cash: {self.cash}, rFactor: {self.rFactor}, ")