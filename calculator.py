def nums(a,b):
    if opertator == "+":
        return a + b
    elif opertator == "-":
        return a - b
    elif opertator == "*":
        return a * b
    elif opertator == "/":
        return a / b

opertator = input("Select your operator(+, -, *, /): ")
a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
print(f"Your answer is {nums(a,b)}")
