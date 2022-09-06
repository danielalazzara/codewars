def queue_time(customers, n):
    queue =[0] * n
    for i in customers:
        queue[0] += i
        queue.sort()
    return max(queue)  
  
