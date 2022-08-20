def tribonacci(signature, n):
    if n == 0:
        return []
    signature = signature[:n]
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature
  
