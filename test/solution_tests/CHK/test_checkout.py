import random
import copy
from checkout import checkout


def test_no_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    p_c = PriceCalculator(prices, {})
    items = 'AAAAABBBBBBBBBBCCCCCCCCCCCCCCCCCCCC'
    assert checkout(items) == 300 + 600 + 3500
    #Lets shuffle to make sure that works
    items_shuffled = copy.copy(items_str)
    random.seed(7)
    random.shuffle(items_shuffled)
    assert checkout(items_shuffled) == 300 + 600 + 3500


def test_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    offers = {'A': (2, 75), 'B': (3, 150)}
    p_c = PriceCalculator(prices, offers)
    items = 'AAAAABBBBBBBBBBCCCCCCCCCCCCCCCCCCCC'
    assert checkout(shuffled) == 225 + 510 + 3500
    #Lets shuffle to make sure that works
    items_shuffled = copy.copy(items_str)

