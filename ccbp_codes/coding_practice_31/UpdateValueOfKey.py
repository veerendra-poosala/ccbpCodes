#UpdateValueOfKey

students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}

update_item = input().split()

students_dict[update_item[0]] = update_item[1]
print(students_dict)