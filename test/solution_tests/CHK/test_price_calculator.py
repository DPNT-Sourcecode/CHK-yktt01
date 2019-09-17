from solutions.CHK.checkout_solution import PriceCalculator, PriceNotFoundError
import pytest

OFFERS = {
    'A': [(2, 75), (1, 50)],
    'B': [(3, 150), (1, 60)],
    'C': [(1, 70)]
}

def test_offers():
    p_c = PriceCalculator(OFFERS)
    assert p_c.calc('A', 6) == 225 
    assert p_c.calc('B', 10) == 510
    assert p_c.calc('C', 20) == 1400

def test_price_not_found():
    p_c = PriceCalculator(OFFERS)
    with pytest.raises(PriceNotFoundError):
        assert p_c.calc('D', 6)


