#basic math operations

def calcu():
    try:
        basic_operation = input("Select operation to be executed: ")
        first_num = float(input("Enter your first number: "))
        second_num = float(input("Enter your second number: "))
    except ValueError as Error:
        print("Invalid number input\n")
        print("ERROR")
        print("\nTry Again")
        return
#ADD
    if basic_operation == "+":
        data_operation = first_num + second_num
        print("The sum of your inputed number is ", data_operation)
#subtract
    elif basic_operation == "-":
        data_operation = first_num - second_num
        print("The difference of your inputed number is ", data_operation)
#multiply
    elif basic_operation == "*":
        data_operation = first_num * second_num
        print("The product of your inputed number is ", data_operation)

#divide
    elif basic_operation == "/":
            data_operation = first_num / second_num
    print(f"Answer: ", + data_operation)

calcu()

#basic math operations
print("Here are the basic math operation to be used:")
print("+ ADD")
print("- SUBTRACT")
print("* MULTIPLY")
print("/ DIVIDE")