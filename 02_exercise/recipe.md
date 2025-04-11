# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def (verify_grammar):
    """

    #verify gammer in string by identifying if the sentance begins with capitol letter and ends with punctuation

    Parameters: (list all parameters and their types)
        pass through a single string in the format of "Test my grammar."

    Returns: (state the return value and its type)
        the return value would be True or False - boolean
        

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

## Given a string with capital letter on first word and punctuation at end
## return value would be True

verify_grammar("Test my grammar.") == True

verify_grammar("test my grammer.") = False

verify_grammar("Test my gammar") = False

verify_grammar("test my grammar") = False
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!

