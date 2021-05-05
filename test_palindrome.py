"""
Unit test for Palindrome Fiinder script.
"""

from Palindrome import PalindromeFinder
import pytest


def test_to_find_palindrome_positive_case():
    """
    Unit test checking for the happy path for palindrome
    with string input.
    """

    expected_for_happy_case = True
    pobject = PalindromeFinder("AMMA")
    result = pobject.to_find_palindrome()
    assert result == expected_for_happy_case
     

def test_to_find_palindrom_negative_case():
    """
    Unit test checking for the unhappy path for palindrome
    with string input.
    """

    expected_for_unhappy_case = False
    pobject = PalindromeFinder("BABY")
    result = pobject.to_find_palindrome()
    assert result == expected_for_unhappy_case


def test_to_find_palindrome_runtime_error():
    """
    Unit test checking for the RuntimeError rasied when the 
    user input is numeric.
    """

    with pytest.raises(RuntimeError):
        pobject = PalindromeFinder(1111)