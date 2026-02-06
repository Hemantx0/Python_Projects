def nums(a,b):
    if opertator == "+":
        return a + b
    elif opertator == "-":
        return a - b
    elif opertator == "*":
        return a * b
    elif opertator == "/":
        return a / b
    else:
        return "Invalid operator"

opertator = input("Select your operator(+, -, *, /): ")
a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
result = nums(a,b)
print(f"Your answer is {result}")
