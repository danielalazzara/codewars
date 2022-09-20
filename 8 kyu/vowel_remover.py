def shortcut( s ):
    vowel = ["a", "e", "i", "o", "u"]
    words = ''
    for l in s:
        if l not in vowel:
            words += l
    return words
    
