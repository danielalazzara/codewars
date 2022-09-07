def bouncing_ball(h, bounce, window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        count = 1
        bouncing = h * bounce
        while bouncing > window:
            bouncing *= bounce
            count += 2
        return count
    else:
        return -1
        
