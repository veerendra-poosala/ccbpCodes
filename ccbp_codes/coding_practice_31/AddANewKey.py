#AddAKey

students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

new_item = input().split()

students_dict[new_item[0]] = new_item[1] #adding new key
print(students_dict)
