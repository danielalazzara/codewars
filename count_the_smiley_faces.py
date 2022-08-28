def count_smileys(arr):
    smileys = []
    for i in arr:
        if len(i) == 2 and i[0] in [':', ';'] and i[1] in[')', 'D']:
            smileys.append(i) 
        elif i[0] in [':', ';'] and i[1] in ['-', '~'] and i[2] in [')', 'D']:
            smileys.append(i) 
    return len(smileys)
  
