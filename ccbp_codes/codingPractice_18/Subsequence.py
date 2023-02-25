#Subsequence

full_line = input()
subsequence_line = input()
length_of_subsequence_line = len(subsequence_line)
#print(length_of_subsequence_line)
subsequence_index = 0
for char in full_line:
    
    if char == subsequence_line[subsequence_index]:
        subsequence_index += 1
        #print(subsequence_index)
        if subsequence_index == length_of_subsequence_line:
            break

if subsequence_index == length_of_subsequence_line:
    print("Yes")
else:
    print("No")