from Palindrome import PalindromeFinder
import pytest
import logging


def test_to_find_palindrome_positive_case():
    expected_for_happy_case = True
    pobject = PalindromeFinder("AMMA")
    result = pobject.to_find_palindrome()
    assert result == expected_for_happy_case
    #logging.info("Case with positive input PASSED.")
     

def test_to_find_palindrom_negative_case():
    expected_for_unhappy_case = False
    pobject = PalindromeFinder("BABY")
    result = pobject.to_find_palindrome()
    assert result == expected_for_unhappy_case

def test_to_find_palindrome_runtime_error():
    with pytest.raises(RuntimeError):
        pobject = PalindromeFinder(1111)







      

            
    

         
