def calc(num1,num2):
    sum = num1 + num2
    diff = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    return sum, diff, product, quotient

num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
sum,diff,product,quotient=calc(num1,num2)

print(f"Sum: {sum}")
print(f"Difference: {diff}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")