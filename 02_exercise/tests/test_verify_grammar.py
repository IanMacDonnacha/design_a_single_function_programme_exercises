from lib.verify_grammar import *

# def test_for_empty_string():
#     result = verify_grammar("")
#     assert result == ""

## Check to see if inital word is capitalised and has punctuation at end
def test_for_capitalised_first_word_and_punctuation_period_at_end():
    result = verify_grammar("Test my grammar.")
    assert result == True

def test_for_capitalised_first_word_and_punctuation_exclamation_mark_at_end():
    result = verify_grammar("Test my grammar!")
    assert result == True

def test_for_capitalised_first_word_and_no_punctuation_period_at_end():
    result = verify_grammar("Test my grammar")
    assert result == False

def test_for_capitalised_first_word_and_no_punctuation_exclamation_mark_at_end():
    result = verify_grammar("Test my grammar")
    assert result == False

def test_for_noncapitalised_first_word_and_punctuation_exclamation_mark_at_end():
    result = verify_grammar("test my grammar!")
    assert result == False

def test_for_noncapitalised_first_word_and_punctuation_period_at_end():
    result = verify_grammar("test my grammar!")
    assert result == False