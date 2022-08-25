def duplicate_count(text):
    lower_text = text.lower()
    count = []
    
    for i in lower_text:
        if not i in count and lower_text.count(i) > 1:               
            count.append(i)
    return len(count)
  
