#ListOfMaximumValues

rows = int(input())
new_list = []

for i in range(rows):
    
    int_list = list(map(int,input().split()))
    maximum = max(int_list)
    new_list += [maximum]
print(new_list)
