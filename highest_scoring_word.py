import string

def high(x):
    letters = string.ascii_lowercase
    sentence = [sum([letters.find(i) + 1 for i in l]) for l in x.split()]
    return x.split()[sentence.index(max(sentence))]
