from collections import Counter
import typing as t

prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

#Tabular price table only allows one offer per item
offers = {
    'A': (3, 130),
    'B': (2, 45),
}

class Pricer:
    def __init__(
        self, prices: t.Mapping[str, int], 
        offers: t.Mapping[str, t.Tuple[int, int]]
    ) _


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    items = Counter(skus)



