from solutions.SUM import sum_solution
import pytest


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_parameter_less_than_zero(self):
        with pytest.raises(ValueError):
            assert sum_solution.compute(-1, 1) 
        with pytest.raises(ValueError):
            assert sum_solution.compute(-1, -1) 
        with pytest.raises(ValueError):
            assert sum_solution.compute(1, -1) 

    def test_parameter_greater_than_one_hundred(self):
        with pytest.raises(ValueError):
            assert sum_solution.compute(101, 1) 
        with pytest.raises(ValueError):
            assert sum_solution.compute(101, 101) 
        with pytest.raises(ValueError):
            assert sum_solution.compute(1, 101) 
