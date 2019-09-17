import random
import copy
from solutions.CHK.checkout_solution import checkout


def test_no_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    items = 'AAAAABBBBBBBBBBCCCCCCCCCCCCCCCCCCCC'
    assert checkout(items, prices=prices, offers={}) == 300 + 600 + 1400
    #Lets shuffle to make sure that works
    items_shuffled = copy.copy(items)
    random.seed(7)
    random.shuffle(items_shuffled)
    assert checkout(items_shuffled) == 300 + 600 + 1400


def test_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    offers = {'A': (2, 75), 'B': (3, 150)}
    items = 'AAAAABBBBBBBBBBCCCCCCCCCCCCCCCCCCCC'
    assert checkout(items, prices=prices, offers=offers) == 225 + 510 + 1400
    #Lets shuffle to make sure that works
    items_shuffled = copy.copy(items)
    assert checkout(items_shuffled) == 225 + 510 + 1400



