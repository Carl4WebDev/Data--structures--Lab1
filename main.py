number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

first_number = int(number1)
second_number = int(number2)

if first_number < second_number:
    print(f"{ first_number } is less than { second_number }")
elif first_number > second_number:
    print(f"{ first_number } is greater than { second_number }")
elif first_number == second_number:
    print(str(first_number) + " is equal to " + str(second_number))

# classmate1 = input("Enter classmate name 1: ")
# classmate2 = input("Enter classmate name 2: ")
# classmate3 = input("Enter classmate name 3: ")
#
# print(f"Your classmates are: {classmate1}, {classmate2}, & {classmate3}")
