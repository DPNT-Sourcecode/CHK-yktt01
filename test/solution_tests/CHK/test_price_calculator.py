from solutions.CHK.checkout_solution import PriceCalculator, PriceNotFoundError
import pytest


def test_offers():
    prices = {'A': 50, 'B': 60, 'C': 70}
    offers = {
        'A': [(2, 75), (1, 50)],
        'B': [(3, 150), (1, 60)],
        'C': [(1, 70)]}
    p_c = PriceCalculator(prices, offers)
    assert p_c.calc('A', 6) == 225 
    assert p_c.calc('B', 10) == 510
    assert p_c.calc('C', 20) == 1400

def test_price_not_found():
    prices = {'A': 50, 'B': 60, 'C': 70}
    p_c = PriceCalculator(prices, {})
    with pytest.raises(PriceNotFoundError):
        assert p_c.calc('D', 6)

