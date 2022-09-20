def is_pangram(s):
    pangram = []
    for i in s.lower():
        if i.isalpha():
            if not i in pangram:
                pangram.append(i)
    return len(pangram) == 26
    
