#SportsData

def updating_dict(students_dict,rows_m):
    
    new_dict = students_dict.copy()
    
    for i in range(rows_m):
        key,value = input().split()
        #print("key: ",key," ","value: ",value)
        for keys in students_dict.keys():
            if keys == key:
                new_dict[key] = value
            else:
                new_dict[key] = value
    return new_dict
        


students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

rows_m = int(input())

new_dict = updating_dict(students_dict,rows_m)
print(new_dict)