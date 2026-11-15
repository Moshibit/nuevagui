from random import shuffle

class Card():
    def __init__(self, rank: int, suit: str) -> None:
        self.__rank: int = rank
        self.__suit: str = suit
        # en algunos juegos como poker el as vale más el rey.
        # en otros como blackjack tiene as tiene valores 1 u 11.
        # esto no está implmentado aquí
        if rank > 10:
            self.__value: int = 10
        else:
            self.__value: int = rank
        if suit == 'S' or suit == 'C':
            self.__color: str = "black"
        else:
            self.__color: str = "red"
        
    def __str__(self) -> str:
        
        return str(self.__rank) + self.__suit

    # def __repr__(self) -> str:
    #     return str(self.__rank) + self.__suit

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        else:
            return False

    @property
    def rank(self):
        return self.__rank

    @property
    def suit(self):
        return self.__suit

    @property
    def value(self):
        return self.__value

    @property
    def color(self):
        return self.__color            


class Deck():

    ranks = [x for x in range(1, 14)]
    suits = ["S", "D", "H", "C"]

    def __init__(self) -> None:
        self.__cards = list()
        for suit in self.suits:
            for rank in self.ranks:
                self.__cards.append(Card(rank, suit))

    # def __str__(self) -> str:
    #     return str(self.__cards)

    # def __repr__(self) -> str:
    #     return str(self.__cards)

    @property
    def cards(self):
        return self.__cards

    def shuffle(self) -> None:
        shuffle(self.__cards)

    def deal(self) -> Card:
        if not self.empty():
            return self.__cards.pop()

    def empty(self) -> bool:
        return self.__cards == []


class Game():
    pass

class Player():
    pass

class Dealer():
    pass

class Table():
    pass

if __name__ == "__main__":
    d = Deck()
    d.shuffle()
    print(d.empty())
    print(d.deal())