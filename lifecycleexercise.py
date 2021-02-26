# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
currentAge = int(age)
maxAge = 90
daysLeft = (maxAge - currentAge) * 365
weeksLeft = (maxAge - currentAge) * 52
monthsLeft = (maxAge - currentAge) * 12

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left")

#or
yearsLeft = (maxAge - currentAge)
#then use the yearsLeft variable in calculation


