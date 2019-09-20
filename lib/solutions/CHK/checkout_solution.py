import typing as t

from collections import Counter
from copy import copy

OfferT = t.Sequence[t.Tuple[int, int]]


#Tabular price table only allows one offer per item
OFFERS = {
    'A': [(5, 200), (3, 130), (1, 50)],
    'B': [(2, 45), (1, 30)],
    'C': [(1, 20)],
    'D': [(1, 15)],
    'E': [(1, 40)],
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
    def __init__(self, offers: t.Mapping[str, OfferT]) -> None:
        self.offers = offers

    @classmethod
    def calc_helper(cls, count: int, offers: t.Mapping[str, OfferT], price=0):
        #This method assumes offers are sorted by number of items
        #Also assumes that for any n for x_a all n+1 for x_b offers have a better rate
        #So x_b/(n+1) is always less than x_a/n
        if not offers:
            return price
        [offer, *rest] = offers
        num_items, offer_price = offer
        num_offers = count // num_items
        remainder_items = count % num_items
        new_price = price + (num_offers * offer_price)
        return cls.calc_helper(remainder_items, rest, new_price) 



    def calc(self, item: str, count: int) -> int:
        try: 
            return PriceCalculator.calc_helper(count, self.offers[item])
        except KeyError as e:
            raise PriceNotFoundError(item) from e


class BuyOfferSpec(t.NamedTuple):
    item: str
    number_required: int


class BuyOfferDiscount(t.NamedTuple):
    item: str
    number_to_discount: int


BuyOfferT = t.Tuple[BuyOfferSpec, BuyOfferDiscount]


BUY_OFFERS = (
    (
        BuyOfferSpec(item='E', number_required=2),
        BuyOfferDiscount(item='B', number_to_discount=1),
    ),
) 

class BuyOfferCalculator:
    """Class which subtracts item counts based buy and get free offers.
       For now we just apply the buy offers in order of specification.
       We are also assuming that there are no transitive buy offers.
       So there can't be a buy offer between A -> B and then B -> C.
    """
    def __init__(self, buy_offers: t.Sequence[BuyOfferT]) -> None:
        self.buy_offers = buy_offers
    
    def subtract_item_counts(self, item_counts: t.Mapping[str, int]) -> t.Mapping[str, int]:
        result = copy(item_counts)
        for buy_offer_spec, buy_offer_discount in self.buy_offers:
            item_count = item_counts.get(buy_offer_spec.item)
            if item_count is None:
                continue
            offer_occurrences = item_count // buy_offer_spec.number_required
            total_to_discount = offer_occurrences*buy_offer_discount.number_to_discount
            result[buy_offer_discount.item] = max(
                result[buy_offer_discount.item] - total_to_discount, 
                0,
            )
        return result
            



# skus = unicode string
def checkout(skus: str, offers=OFFERS, buy_offers=BUY_OFFERS) -> int:
    if not isinstance(skus, str):
        return -1
    price_calculator = PriceCalculator(offers)
    buy_offer_calculator = BuyOfferCalculator(buy_offers)
    item_counts = Counter(skus)
    item_counts_buy_offers = buy_offer_calculator.subtract_item_counts(item_counts)
    try:
        price = sum(
            price_calculator.calc(item, count) 
            for item, count in item_counts.items()
        )
        price_with_buy_offers = sum(
            price_calculator.calc(item, count) 
            for item, count in item_counts_buy_offers.items()
        )
        return min(price, price_with_buy_offers)
    except PriceNotFoundError:
        return -1



