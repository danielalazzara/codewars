def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if year_of_birth ==  current_year:
        return "You were born this very year!"
    elif current_year == year_of_birth + 1:
        return f"You are {age} year old."
    elif current_year > year_of_birth:
        return f"You are {age} years old."
    elif current_year + 1 == year_of_birth:
        return f"You will be born in {abs(age)} year."
    else: 
        return f"You will be born in {abs(age)} years."
