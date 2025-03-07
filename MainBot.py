class Bot():
    def __init__(self, randomFactor, riskFactor, min, max, cash, seat, hands):
        self.riskFactor = riskFactor
        self.randomFactor = randomFactor
        self.min = min
        self.max = max
        self.cash = cash
        self.seat = seat
        self.handsPlayed = hands

    def newHand(self, hand, blind):
        self.hand = hand
        self.pot = 3 * min
        self.blind = blind
        if blind == "B":
            self.bet(min * 2)
        elif blind == "b":
            self.bet(min)

    def CalcBet(self, round):
        #isAnte?
        return self.bet()
    
    def bet(self, amt):
        betAmt = self.min
        self.cash -= betAmt
        return betAmt
    
    def stats(self):
        print("Cash: {self.cash}, rFactor: {self.rFactor}, ")