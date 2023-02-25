#ExtractDigits

given_line = input()

digits_list = []

for char in given_line:
    if char.isdigit():
        digits_list += [int(char)]
#print(digits_list)
total_of_digits = sum(digits_list)
minimum = min(digits_list)
maximum = max(digits_list)
print(total_of_digits)
print(minimum)
print(maximum)