print(len("RAM"))
print(len("12345"))
#DATA TYPES: 1 string, 2 integer, 3 float, 4 boolean
#string
print("hello"[0])
print("hello"[1])
print("hello"[2])
print("hello"[3])
print("hello"[4])
print("hello"[-1])
print("hello"[-2])
print("hello"[-3])
print("hello"[-4])
print("hello"[-5])
print("123" + "456") #answer 123456 string concatenate
#integer data types: may be negative or positive but without decimal point
print(123 + 456) #answer summation
#float data types :
print("3.1415")
print("7110.1415")
#boolean data types: start with capital latter without any coatation mark
print("true")
print("false")
# write a program to calculate the user input name to show the number of characters
num_char=len(input("enter your name "))
new_num_char=str(num_char)
print("your name have "+ new_num_char+" characters")
#or
num_char=str(len(input("enter your name ")))
print("your name have "+ num_char+" characters")
print(70+float("100.5"))
print(str(100)+str(100)) #answer would be 100100
# write a program that add the digits in a two digit number, e.g if the input is 35 then the output should be 3+5=8
two_digit_number = input("enter two digit number: ")
fst_digit_num = two_digit_number[1]
scnd_digit_num = two_digit_number[0]
result = int(fst_digit_num) + int(scnd_digit_num)
print(result)
#write a program to find user bmi(body mass index= weight/height square)
height= input("enter your height in m: ")
weight= input("enter your weight in kg: ")
bmi=float(weight) / float(height)**2
print(bmi)
#arithimatic operation:
print(int(3/2))
print(round(2.6666 ,3 ))
# to get intiger result during division operation
print(8//3) #use double backslash
# f-string:
score=0
height=1.8
isWinning=True
print(f"your score is {score},your height is {height} and you are Winning {isWinning}")
#create a program using math and f-string that tells us how many days ,weeks and months left if we live 90yr old
age = input("enter your age: ")
age_as_int = int(age)
remaining_age_in_yr = 90 - age_as_int
remaining_age_in_days = remaining_age_in_yr * 365
remaining_age_in_weeks = remaining_age_in_yr * 52
remaining_age_in_month = remaining_age_in_yr * 12
message = f"you have {remaining_age_in_days} days,or {remaining_age_in_weeks} weeks,or {remaining_age_in_month} month left"
print(message)
#create a program of TIPS_calculator:
# welcome to the tips calculator
# what was the total bill: ₹150
# what percentage tips would you like to give : 10,12 or 15 %
# how many people you wanna to split the bills:
# each person should pay ₹21.35
print("welcome to the tips calculator:")
bill = float(input("what is the total bill ₹ "))
tip = int(input("what percentage would you like to give tips 10,12 or 15 ?"))
people = int(input("how many people you wanna to split the bill: "))
bill_with_tip = tip/100 * bill + bill
# bill_with_tip = bill * ( tip/100 + 1 )
bill_per_person = round(bill_with_tip / people , 2)
print(f"bill per person have to pay: ₹{bill_per_person}")

