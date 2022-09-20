def DNA_strand(dna):
    complements = {
        "A":"T",
        "T":"A",
        "C":"G",
        "G":"C"
    }
    return ''.join([complements[i] for i in dna])
  
