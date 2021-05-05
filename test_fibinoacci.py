"""
Unit test for Fibinoacci Series script
"""

from FibinoacciSeries import FibinoacciSeries
import logging
import pytest

def test_to_print_fseries_integer_input():
    """
    pytest method to check for happy path
    """

    fobject = FibinoacciSeries(3)
    output_list = fobject.to_print_fseries()
    assert output_list == [0,1,1]
    logging.info("Actual result is equal to Expected result")

def test_to_print_fseries_string_input():
    """
    pytest method to check for unhappy path
    """

    with pytest.raises(RuntimeError):
        fobject = FibinoacciSeries("A")

    


