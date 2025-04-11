# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python


def reading_time(string):
    ### Determine reading time of string for 200 words/min

    Parameters: (list all parameters and their types)
        string - containg a sentance of words.

    Returns: (state the return value and its type)
        the return value will be an integer i.e time take to read string

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    
    pass 
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

#if we through an empty string we should receive a value of 0

reading_time(" ") == 0


#taking 11 words, the resulting value should be 11/200

reading_time("Hello, I am a string and have a certain reading time") == 0.055 

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python

from lib.reading_time import *

def test_reading_time_for_empty_string():
    result = reading_time("")
    assert result == 0


```

Ensure all test function names are unique, otherwise pytest will ignore them!




