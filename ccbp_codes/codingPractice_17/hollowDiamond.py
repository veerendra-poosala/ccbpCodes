#hollowDiamond

cols_n = int(input())
rows_n = (2*cols_n)-1
#top part
left_spaces = " "*(cols_n-1)
print(left_spaces+"* ")

#middle part
hollow_spaces_count = 1
for i in range(1,cols_n):
    left_spaces = " "*(cols_n-i-1)
    stars ="*"
    hollow_spaces = " "*hollow_spaces_count
    #print(left_spaces+stars)
    print(left_spaces+stars+hollow_spaces+stars)
    hollow_spaces_count = hollow_spaces_count +2

#bottom part
hollow_spaces_count = hollow_spaces_count -2
for j in range(1,cols_n-1):
    left_spaces = " "*(j)
    hollow_spaces_count = hollow_spaces_count - 2
    hollow_spaces = " "*hollow_spaces_count
    stars ="*"
    print(left_spaces+stars+hollow_spaces+stars)

left_spaces = " "*(cols_n-1)
print(left_spaces+"*")
