from solutions.SUM import sum_solution
import pytest


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_para_boundaries(self):
        with pytest.raises(ValueError):
            assert sum_solution(-1, 1) 
        with pytest.raises(ValueError):
            assert sum_solution(-1, -1) 

