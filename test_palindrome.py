from Palindrome import PalindromeFinder
import pytest


def test_to_find_palindrome():

    dict = {"positive_example" : "Madam, I'm Adam!!", "negative_example" : "Boys","runtime_error":1111}  
    expected_for_happy_case = True 
    expected_for_unhappy_case = False
    for each_in_dict in dict:
        if each_in_dict == "positive_example":
            pobj = PalindromeFinder(dict[each_in_dict])
            result = pobj.to_find_palindrome()
            assert result == expected_for_happy_case
            print("Case 1: PASSED")
        if each_in_dict == "negative_example":
            pobj = PalindromeFinder(dict[each_in_dict])
            result = pobj.to_find_palindrome()
            assert result == expected_for_unhappy_case    
            print("Case 2: PASSED")
        if each_in_dict == "runtime_error":
            with pytest.raises(RuntimeError):
                pobj = PalindromeFinder(dict[each_in_dict])
            print("Case 2: PASSED")
    



      

            
    

         
