vowels = {'a':'1', 'e':'2', 'i':3, 'o':'4', 'u':'5'}

def encode(st):
    for w in vowels:
        st = st.replace(w, str(vowels[w]))
    return st
    
def decode(st):
    for k,v in vowels.items():
        st = st.replace(str(v), str(k))
    return st
  
