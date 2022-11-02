#LastHalfOfList

n = int(input())

new_list = []

number = input().split()
#print(number)

#converting string datatype into integer datatype
for i in number:
    i = int(i)
    new_list += [i]
#print(new_list)

half_length = int((n)/2 )
#print(half_length)



if n % 2 == 0:
    list_2 = new_list[half_length:]
    print(list_2)
else:
    half_length = half_length + 1
    list_2 = new_list[(half_length):]
    print(list_2)
