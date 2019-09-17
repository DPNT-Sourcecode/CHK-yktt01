from collections import Counter
import typing as t

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

OfferT = t.Tuple[int, int]


#Tabular price table only allows one offer per item
OFFERS = {
    'A': (3, 130),
    'B': (2, 45),
}

class BaseException(Exception):
    pass


class PriceNotFoundError(BaseException):
    def __init__(self, item: str) -> None:
        super().__init__(self, item)
        self.item = item
        self.msg = "No price for {0} found".format(self.item)

    def __str__(self) -> str:
        return self.msg


class PriceCalculator:
    def __init__(
        self, prices: t.Mapping[str, int], 
        offers: t.Mapping[str, OfferT]
    ) -> None:
        self.prices = prices
        self.offers = offers

    def calc(self, item: str, count: int) -> int:
        try: 
            offer = self.offers.get(item)
            if offer is None:
                return self.prices[item] * count
            num_items, offer_price = offer
            num_offers = count // num_items
            remainder_items = count % num_items
            return (num_offers * offer_price) + remainder_items * self.prices[item]
        except KeyError as e:
            raise PriceNotFoundError(item) from e


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str, prices=PRICES, offers=OFFERS) -> int:
    if not isinstance(skus, str):
        return -1
    price_calculator = PriceCalculator(prices, offers)
    item_counts = Counter(skus)
    try:
        return sum(
            price_calculator.calc(item, count) 
            for item, count in item_counts.items()
        )
    except PriceNotFoundError:
        return -1





