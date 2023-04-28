def rain_amount(mm):
    rain = 40 - mm
    if (mm < 40):
         return f"You need to give your plant {rain}mm of water"
    else:
         return "Your plant has had more than enough water for today!"
      
