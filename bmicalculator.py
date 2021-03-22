# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float((weight) / (height ** 2))
print("Your bmi is " + str(bmi))
#OR
print(f"Your bmi is {bmi}")
if bmi < 18.5:
  print("You are underweight.")
elif bmi > 18.5 and bmi < 25:
  print("You are normal weight.")
elif bmi > 25 and bmi <30:
  print("You are slightly overweight.")
elif bmi > 30 and bmi < 35:
  print("You are obese.")
else:
  print("You are clinically obese.")