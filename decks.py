def buildDeck():
    suits = ["H", "D", "S", "C"]
    numbers = list(range(1,10))
    faceCards = ["K", "Q", "J"]
    ace = "A"
    deck = list()
    for suit in suits:
        for number in numbers:
            deck.append(f"{suit}{number}")
        for faceCard in faceCards:
            deck.append(f"{suit}{faceCard}")
        deck.append(f"{suit}{ace}")
    return deck

def buildDecks(numberOfDecks):
    deck = list()
    for _ in range(numberOfDecks):
        deck.extend(buildDeck())
    return deck

if __name__ == "__main__":
    print(len(buildDecks(2)))