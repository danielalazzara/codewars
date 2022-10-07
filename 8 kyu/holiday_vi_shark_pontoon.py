def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
    if shark_distance / shark_speed > pontoon_distance / you_speed:
        return "Alive!"
    return "Shark Bait!"
  
