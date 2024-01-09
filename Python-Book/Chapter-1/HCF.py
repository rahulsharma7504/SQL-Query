a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

# Find the maximum and minimum of the two numbers
max_num = max(a, b)
min_num = min(a, b)

dividend = max_num
divisor = min_num

while dividend % divisor != 0:
    remainder = dividend % divisor
    dividend = divisor
    divisor = remainder

hcf = divisor

print(f'The HCF of {a} and {b} is: {hcf}')
