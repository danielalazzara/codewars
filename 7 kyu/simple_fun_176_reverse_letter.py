def reverse_letter(string):
    return ''.join([n for n in string[::-1] if n.isalpha()]) 
