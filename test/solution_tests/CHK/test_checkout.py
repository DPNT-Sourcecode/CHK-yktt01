import random
import pytest
from solutions.CHK.checkout_solution import checkout


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
    assert checkout(items, offers=OFFERS) == 225 + 510 + 1400
    #Lets shuffle to make sure that works
    items_shuffled = shuffle_str(items)
    assert checkout(items_shuffled, offers=OFFERS) == 225 + 510 + 1400


def test_price_not_found():
    prices = {'A': 50, 'B': 60, 'C': 70}
    items = 'A'*6 + 'B'*10 + 'C' * 20 + 'D'
    assert checkout(items, offers=OFFERS) == -1
