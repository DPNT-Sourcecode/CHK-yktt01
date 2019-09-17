from checkout import checkout
from random import shuffle


def test_no_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    p_c = PriceCalculator(prices, {})
    assert checkout('AAAAABBBBBBBBBBCCCCCCCCCCCCCCCCCCCC')== 300 + 600 + 3500

def test_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    offers = {'A': (2, 75), 'B': (3, 150)}
    p_c = PriceCalculator(prices, offers)
    assert checkout('AAAAABBBBBBBBBBCCCCCCCCCCCCCCCCCCCC')) == 225 + 510 + 3500
