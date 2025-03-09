import findHand

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
    
    def calcHands(self, deck, hand, pool, players):
        # highcard, pair, 2p, 3x, straight, full house, flush, 4x, royal flush
        # 0,        1,    2,  3,  4,        5,          6,     7,  8
        deck.size()
        
        #for i in range(0, 9):
            #print(i)

    def bet(self, amt):
        betAmt = self.min
        self.cash -= betAmt
        return betAmt
    
    def stats(self):
        print("Cash: {self.cash}, rFactor: {self.rFactor}, ")

    def CalcBet(self, round):
        #isAnte?
        return self.bet()
    
    def hand(self, pool):
        findHand.find(pool)