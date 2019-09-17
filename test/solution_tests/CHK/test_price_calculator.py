from checkout import PriceCalculator

def test_no_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    p_c = PriceCalculator(prices, {})
    assert p_c.calc({'A': 6, 'B': 10, 'C': 20})