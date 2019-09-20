from solutions.CHK.checkout_solution import (
    BuyOfferCalculator, BuyOfferSpec, BuyOfferDiscount,
)

BUY_OFFERS = (
    (
        BuyOfferSpec(item='A', number_required=2),
        BuyOfferDiscount(item='B', number_to_discount=1),
    ),
    (
        BuyOfferSpec(item='C', number_required=1),
        BuyOfferDiscount(item='D', number_to_discount=4),
    ),
) 

def test_buy_offer_calculator():
    buy_offer_calculator = BuyOfferCalculator(BUY_OFFERS)
    item_counts = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 10,
    }
    result = buy_offer_calculator.subtract_item_counts(item_counts)
    assert result == {
        'A': 7,
        'B': 3,
        'C': 2,
        'D': 2,
    }

def test_empty_buy_offer_calculator():
    buy_offer_calculator = BuyOfferCalculator([])
    item_counts = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 10,
    }
    result = buy_offer_calculator.subtract_item_counts(item_counts)
    assert result == item_counts