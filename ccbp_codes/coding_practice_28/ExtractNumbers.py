#ExtractNumbers

def extract_numbers(given_list):
    int_list = []
    
    for char in given_list:
        if char.isdigit():
            char = int(char)
            int_list += [char]
    return sorted(int_list)


#Taking comma-separated strings as user input 

given_list = input().split(",")

result = extract_numbers(given_list)
print(result)
