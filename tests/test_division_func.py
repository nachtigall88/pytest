from utils import division
import pytest


@pytest.mark.parametrize('a, b, expected_result', [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize('expected_exception, divider', [(ZeroDivisionError, 0),
                                                         (TypeError, '2')])
def test_division_with_error(expected_exception, divider):
    with pytest.raises(expected_exception):
        division(10, divider)
