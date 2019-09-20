from collections import Counter
import typing as t

OfferT = t.Sequence[t.Tuple[int, int]]


#Tabular price table only allows one offer per item
OFFERS = {
    'A': [(5, 150), (3, 130), (1, 50)],
    'B': [(2, 45), (1, 30)],
    'C': [(1, 20)],
    'D': [(1, 15)],
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

class BuyNgetMFree:
    """Class which subtracts item counts based buy and get free offers.
       For now we just apply the buy offers in order of specification
    """
    def __init__(self, buy_offers) -> None:
        self.buy_offers = buy_offers
    
    def subtract_item_counts(item_counts: t.Sequence[BuyOfferT]):
        for buy_offer_spec, buy_offer_discount in self.buy_offers:
            fore


# skus = unicode string
def checkout(skus: str, offers=OFFERS) -> int:
    if not isinstance(skus, str):
        return -1
    price_calculator = PriceCalculator(offers)
    item_counts = Counter(skus)
    try:
        return sum(
            price_calculator.calc(item, count) 
            for item, count in item_counts.items()
        )
    except PriceNotFoundError:
        return -1






