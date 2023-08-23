# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
life_left = f" You have {(90 * 365) - (age_as_int * 365)} days, {(90 * 52) - (age_as_int * 52)} weeks, and {(90 * 12) - (age_as_int * 12)} months left."
print(life_left)