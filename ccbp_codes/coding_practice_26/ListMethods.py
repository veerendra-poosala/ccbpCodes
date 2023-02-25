#ListMethods

num_list = []

n = int(input())

for i in range(n):
    command = input().split()
    #print(command)
    #print(command[0])

    if command[0] == "insert":
        index = int(command[1])
        value = int(command[2])
        num_list.insert(index,value)

    elif command[0] == "append":
        value = int(command[1])
        num_list.append(value)

    elif command[0] == "pop":
        num_list.pop()

    elif command[0] == "remove":
        value = int(command[1])
        num_list.remove(value)

    elif command[0] == "sort":
        num_list.sort()
        
    elif command[0] == "print":
        print(num_list)
