def verify_grammar(string):
    if string[0] == string[0].upper() and string[-1] in ".!":
            return True
    else:
        return False

 
    