#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(type(two_digit_number))
print(int(two_digit_number[0]) + int(two_digit_number[1]))

#OR
print("------")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

two_digit_number = first_digit + second_digit
print(two_digit_number)