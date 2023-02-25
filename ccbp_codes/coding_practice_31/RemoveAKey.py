#RemoveAKey

students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}

del_key = input()

dict_b = students_dict.copy()

for key in students_dict.keys():
    if key == del_key:
        del dict_b[key]


print(dict_b)
