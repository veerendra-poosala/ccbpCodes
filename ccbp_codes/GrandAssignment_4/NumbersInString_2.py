#NumbersInString_2

def get_sum_and_avg_of_nums_in_str(given_string):
    num_list = []
    string_list = given_string.split()
    #print("string_list",string_list,"length",len(string_list))
    char_pos = 0
    counter = 0
    while counter < len(given_string):
        num = ""
        for j in range(char_pos,len(given_string)):
            char = given_string[j]
            #print("char",char)
            is_upper = char == char.upper()
            is_lower = char == char.lower()
            is_special_char = is_upper and is_lower
            char_pos = j+1 #holding previous position
            
            if char.isdigit():
                num += char
                #print("num",num)
            elif char.isdigit() == False:
                break
            elif is_special_char == True:
                #print("char",char," ",is_special_char)
                break
                
        if num.isdigit():
            n = int(num)
            num_list += [n]
        counter += 1
        
    #print("num_list",num_list)
    total = sum(num_list)
    length_of_nums = len(num_list)
    avg = round((total / length_of_nums),2)
    print(total)
    print(avg)

given_string = input()

result = get_sum_and_avg_of_nums_in_str(given_string)
