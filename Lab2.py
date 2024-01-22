def human_to_dog_age(human_age):
    dog_age_years = int(human_age * 7)

    remaining_months = (human_age * 7 - dog_age_years) * 12
    dog_age_months = int(remaining_months)
    dog_age_days = int((remaining_months - dog_age_months) * 30)

    return dog_age_years, dog_age_months, dog_age_days

user_human_age = float(input("Enter your age on Pythoid: "))
dog_age_result = human_to_dog_age(user_human_age)
print(f"The dog age on planet Pythoid is {dog_age_result[0]} years, {dog_age_result[1]} months, and {dog_age_result[2]} days.")

def human_to_cat_age(human_age):
    cat_age_years = int(human_age / 9)

    remaining_months = (human_age / 9 - cat_age_years) * 12
    cat_age_months = int(remaining_months)
    cat_age_days = int((remaining_months - cat_age_months) * 30)

    return cat_age_years, cat_age_months, cat_age_days

user_human_age = float(input("Enter your age on Pythoid: "))
cat_age_result = human_to_cat_age(user_human_age)
print(f"The cat age on planet Pythoid is {cat_age_result[0]} years, {cat_age_result[1]} months, and {cat_age_result[2]} days.")

def human_to_horse_age(human_age):
    horse_age_years = int((3 * (human_age ** 2) - 47) / 7) + 12
    
    remaining_months = (3 * (human_age ** 2) - 47) % 7 * 12
    horse_age_months = int(remaining_months)
    horse_age_days = int((remaining_months - horse_age_months) * 30)
    
    return horse_age_years, horse_age_months, horse_age_days

# Example usage
user_human_age = float(input("Enter your age: "))
horse_age_result = human_to_horse_age(user_human_age)
print(f"The horse age is {horse_age_result[0]} years, {horse_age_result[1]} months, and {horse_age_result[2]} days.")
