def domain_name(url):
    url_split = url.split('.')
    if url_split[0][:3] == 'htt':
        if url_split[0].split('//')[1] == 'www':
            return url_split[1]
        if 'https' in url_split[0]:
            url_split[0] = url_split[0][8:]
        if 'http' in url_split[0]:
            url_split[0] = url_split[0][7:]
        return url_split[0]
    if url_split[0][:3] == 'www':
        return url_split[1]
    return url_split[0]
  
