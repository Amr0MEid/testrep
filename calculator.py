#calculator

def calculate(num1,op,num2):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    elif op == '/':
        if num2!= 0:
            return num1/num2
        else:
            return "Error!!! Divide by zero"
    else:
        return "error!! wrong operator"
num1 = eval(input("please enter num1: "))
op = input("please enter the operator: ")
num2 = eval(input("please enter num2: "))
print(calculate(num1,op,num2))