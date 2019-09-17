import random
import pytest
from solutions.CHK.checkout_solution import checkout


def shuffle_str(s: str) -> str:
    random.seed(7)
    li = list(s)
    random.shuffle(li)
    return str.join('', li)


def test_no_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    items = 'A'*6 + 'B'*10 + 'C' * 20
    assert checkout(items, prices=prices, offers={}) == 300 + 600 + 1400
    #Lets shuffle to make sure that works
    items_shuffled = shuffle_str(items)
    assert checkout(
        items_shuffled, prices=prices, offers={},
    ) == 300 + 600 + 1400


def test_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    offers = {'A': (2, 75), 'B': (3, 150)}
    items = 'A'*6 + 'B'*10 + 'C' * 20
    assert checkout(items, prices=prices, offers=offers) == 225 + 510 + 1400
    #Lets shuffle to make sure that works
    items_shuffled = shuffle_str(items)
    assert checkout(
        items_shuffled, prices=prices, offers=offers,
    ) == 225 + 510 + 1400

def test_price_not_found():
    prices = {'A': 50, 'B': 60, 'C': 70}
    items = 'A'*6 + 'B'*10 + 'C' * 20 + 'D'
    assert checkout(items, prices=prices, offers={}) == -1