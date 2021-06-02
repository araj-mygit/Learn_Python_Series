from unique_word_count import FindUniqueWordCount
import pytest
import os 
import sys

input_text_file_with_tooltip_reference = os.path.join(sys.path[0], "Inputs","input_with_reference.txt")
input_file_with_tooltip_reference = os.path.join(sys.path[0], "Inputs", "input_with_tooltip_reference.txt")
input_file_with_whitespace = os.path.join(sys.path[0], "Inputs", "input_with_whitespace.txt") 
set_of_unique_words = {'quantum', 'able', 'are', 'be', 'believed', 'certain', 'computational', 'computers','problems', 'solve', 'they', 'to'}


def test_check_file_extension():

    """
    Pytest to check the input file extension is .txt or not
    """

    loaded_input = FindUniqueWordCount(input_text_file_with_tooltip_reference)
    output = loaded_input.check_file_extension()
    assert output == True


def test_remove_tooltip_reference():

    """
    Pytest to remove all the tooltip references in input file.
    """

    loaded_input = FindUniqueWordCount(input_file_with_tooltip_reference)
    output = loaded_input.remove_tooltip_reference()
    assert output == "Quantum computers They are believed to be able to solve certain computational problems "


def test_remove_whitespace_from_string():

    """
    Pytest to remove whitespace if-any form input file and
    convert the words to small letters.
    """
    
    loaded_input = FindUniqueWordCount(input_file_with_whitespace)
    output = loaded_input.remove_whitespace_from_string()
    assert output == "quantum computers they are believed to be able to solve certain computational problems"


def test_get_set_of_unique_word():

    """
    Pytest to get set of unique words form input file.
    """

    loaded_input = FindUniqueWordCount(input_file_with_whitespace)
    output = loaded_input.get_set_of_unique_word()
    assert output == set_of_unique_words


def test_find_unique_word():

    """
    Pytest to create a text file and append the unique words to it.
    """

    loaded_input = FindUniqueWordCount(input_file_with_whitespace)
    output_file_generated = loaded_input.find_unique_word()
    assert "UniquewordCount.txt" in (sys.path[0] + "/UniquewordCount.txt")