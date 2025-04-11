import pytest
from lib.reading_time import *

def test_reading_time_for_empty_string():
    result = reading_time("")
    assert result == 0

def test_reading_time_for_string_of_11_words():
    word_count = " ".join(["word" for i in range(0, 11)])
    result = reading_time(word_count)
    assert result == 0.055

def test_reading_time_for_string_of_200_words():
    word_count = " ".join(["word" for i in range(0, 200)])
    result = reading_time(word_count)
    assert result == 1.0

def test_reading_time_fail_for_none_passed_as_argument():
    with pytest.raises(Exception) as e:
        reading_time(None)
    error_msg = str(e.value)
    assert error_msg == "Not a string" 