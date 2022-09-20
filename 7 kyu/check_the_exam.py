def check_exam(arr1,arr2):
    total = 0
    for i, j in zip(arr1,arr2):
        if j == '':
            continue
        elif i == j:
            total += 4
        else:
            total -= 1
    return total if total > 0 else 0
    
