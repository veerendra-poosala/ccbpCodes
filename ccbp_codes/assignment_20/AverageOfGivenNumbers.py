#AverageOfGivenNumbers

given_list = input().split()

length = len(given_list)

sum = 0
for num in given_list:
    num = int(num)
    sum += num

average =round( (sum / length),2)
print(average)