def warn_the_sheep(queue):
    queue.reverse()
    wolf_position = queue.index("wolf")
    if wolf_position == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        return "Oi! Sheep number " + str(wolf_position) + "! You are about to be eaten by a wolf!"
