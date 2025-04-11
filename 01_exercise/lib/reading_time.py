def reading_time(string):
    if string is None:
        raise Exception("Not a string")
        
    split_string = string.split()
    reading_time = len(split_string)/200
    return reading_time