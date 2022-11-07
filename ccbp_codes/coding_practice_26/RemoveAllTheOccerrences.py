#RemoveAllTheOccerrences

nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
# Write your code here
number = int(input())
count = nums_list.count(number)
#print(count)
for i in range(count):
    nums_list.remove(number)
print(nums_list)