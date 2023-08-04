#basic math operations
print("Here are the basic math operation to be used:")
print("+ ADD")
print("- SUBTRACT")
print("* MULTIPLY")
print("/ DIVIDE")


def calcu():

    first_num = float(input("Enter your first number: "))
    second_num = float(input("Enter your second number: "))

    basic_operation = input("Select operation to be executed: ")
#ADD
    if basic_operation == "+":
        data_operation = first_num + second_num
    
    print(f"Answer: ", + data_operation)

#subtract
#multiply
#divide

calcu()