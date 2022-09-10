def gimme(input_array):
    if len(input_array) == 3:
        return input_array.index(sorted(input_array)[1])
    
