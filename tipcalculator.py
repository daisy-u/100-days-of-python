#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

bill = float(input("What is your total bill? "))
people = int(input("How many people are splitting this bill? "))
tip = int(input("What percentage are you tipping? "))

# print(type(bill))
# print(type(people))
# print(type(tip))

totalBill = (bill + (bill * (tip / 100)))
#eachTip = round(totalBill / people, 2)
eachTip = "{:.2f}".format(totalBill /people)
print(f"Your total bill is {totalBill} ")
print(f"Each person should pay {eachTip}")
