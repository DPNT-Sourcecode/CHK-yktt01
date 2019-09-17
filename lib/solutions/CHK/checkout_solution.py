from collections import Counter
import typing as t

prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

OfferT = t.Tuple[int, int]


#Tabular price table only allows one offer per item
offers = {
    'A': (3, 130),
    'B': (2, 45),
}


class PriceCalulator:
    def __init__(
        self, prices: t.Mapping[str, int], 
        offers: t.Mapping[str, OfferT]
    ) -> None:
        self.prices = prices
        self.offers = offers

    def calc(item: str, count: int) -> int:
        offer = self.offers.get(item)
        if offer is None:
           return self.prices[item] * count
        num_items, offer_price = offer
        num_offers = count // num_items


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    items = Counter(skus)





