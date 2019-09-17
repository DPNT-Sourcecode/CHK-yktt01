from solutions.CHK.checkout_solution import PriceCalculator

def test_no_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    p_c = PriceCalculator(prices, {})
    assert p_c.calc('A', 6) == 300 
    assert p_c.calc('B', 10) == 600
    assert p_c.calc('C', 20) == 1400

def test_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    offers = {'A': (2, 75), 'B': (3, 150)}
    p_c = PriceCalculator(prices, offers)
    assert p_c.calc({'A': 6, 'B': 10, 'C': 20}) == 225 + 510 + 1400
    assert p_c.calc('A', 6) == 225 
    assert p_c.calc('B', 10) == 510
    assert p_c.calc('C', 20) == 1400


