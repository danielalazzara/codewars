def count_positives_sum_negatives(arr):
    return [len([n for n in arr if n > 0]), sum([n for n in arr if n < 0])] if not len(arr) == 0 else [] 
        
