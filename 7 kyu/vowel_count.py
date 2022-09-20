def get_count(sentence):
    total = 0
    for vowel in ["a", "e", "i", "o", "u"]:
        total += sentence.count(vowel)
    return total
  
