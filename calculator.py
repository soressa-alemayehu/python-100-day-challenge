
#add
def add(n1, n2):
    return n1 + n2
#sub
def sub(n1, n2):
    return n1 -n2 
#mult
def mult(n1, n2):
    return n1 * n2 
#divide
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    }
cont = True
should_continue = True
    
number1 = int(input("input number: "))

for op in operations:
    print(op)
while should_continue:
    operation_symbol = input("pick an operation: ")

    number2 = int(input("\n input number: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(number1, number2)
    print(f"{number1} {operation_symbol} {number2} = {answer}")

    choose = input("Do you want to contine (y/n)")
    if choose == "y":
        number1 == answer
    elif choose == 'n':
        should_continue == False
    else: 
        print("error")
