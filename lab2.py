class Card(object):
    """Одна игральная карта"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.total = Card.RANKS.index(self.rank) + 1

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand(object):
    """Рука: набор игральных карт"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep = "  ".join(card)
        else:
            rep = "<пусто>"
        return rep

    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """Колода карт"""
    def fill(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
                #print(Card(rank,suit))
                #print(self.cards)

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Нет больше карт")