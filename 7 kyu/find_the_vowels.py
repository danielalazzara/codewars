def vowel_indices(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels_count = []
    for i, v in enumerate(word):
        if v in vowels or v in [x.upper() for x in vowels]:
            vowels_count.append(i + 1)
    return vowels_count
  
