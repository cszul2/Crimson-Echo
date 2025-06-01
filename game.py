class Player:
    def __init__(self):
        self.score = 0
    
class Dealer(Player):
    def __init__(self):
        super().__init__()

def getCardValue(card):
    order = card[1:]
    numbers = list(range(1,10))
    if order in ["H", "D", "S", "C"]:
        value = 10
    if order in numbers:
        value = int(order)
    if order in ["A"]:
        value = 11