numbers = [10, 20, 4, 45, 99]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print("The largest number in the list is:", largest_number)
