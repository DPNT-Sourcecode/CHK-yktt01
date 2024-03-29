import random
import pytest
from solutions.CHK.checkout_solution import (
    checkout, BuyOfferSpec, BuyOfferDiscount,
)


def shuffle_str(s: str) -> str:
    random.seed(7)
    li = list(s)
    random.shuffle(li)
    return str.join('', li)


OFFERS = {
    'A': [(2, 75), (1, 50)],
    'B': [(3, 150), (1, 60)],
    'C': [(1, 70)]
}


def test_offers():
    items = 'A'*6 + 'B'*10 + 'C' * 20
    assert checkout(items, offers=OFFERS, buy_offers=[]) == 225 + 510 + 1400
    #Lets shuffle to make sure that works
    items_shuffled = shuffle_str(items)
    assert checkout(items_shuffled, offers=OFFERS, buy_offers=[]) == 225 + 510 + 1400

def test_offers1():
    offers = {
        'A': [(5, 200), (3, 130), (1, 50)],
    }
    items = 'A'*5 
    assert checkout(items, offers=offers, buy_offers=[]) == 200
    #Lets shuffle to make sure that works
    items_shuffled = shuffle_str(items)
    assert checkout(items_shuffled, offers=offers, buy_offers=[]) == 200


def test_price_not_found():
    items = 'A'*6 + 'B'*10 + 'C' * 20 + 'D'
    assert checkout(items, offers=OFFERS, buy_offers=[]) == -1


def test_applying_buy_offer_is_cheaper():
    buy_offers = (
        (
            BuyOfferSpec(item='A', number_required=3),
            BuyOfferDiscount(item="B", number_to_discount=1),
        ),
    )
    items = 'A'*6 + 'B'*10 + 'C' * 20
    assert checkout(items, offers=OFFERS, buy_offers=buy_offers) == 225 + 420 + 1400
    #Lets shuffle to make sure that works
    items_shuffled = shuffle_str(items)
    assert checkout(items_shuffled, offers=OFFERS, buy_offers=buy_offers) == 225 + 420 + 1400


def test_applying_buy_offer_is_not_cheaper():
    offers = {
        'A': [(2, 75), (1, 50)],
        'B': [(10, 5), (1, 60)], # a really contrived example I know
        'C': [(1, 70)]
    }
    buy_offers = (
        (
            BuyOfferSpec(item='A', number_required=6),
            BuyOfferDiscount(item="B", number_to_discount=1),
        ),
    )
    items = 'A'*6 + 'B'*10 + 'C' * 20
    assert checkout(items, offers=offers, buy_offers=buy_offers) == 225 + 5 + 1400
    #Lets shuffle to make sure that works
    items_shuffled = shuffle_str(items)
    assert checkout(items_shuffled, offers=offers, buy_offers=buy_offers) == 225 + 5 + 1400
