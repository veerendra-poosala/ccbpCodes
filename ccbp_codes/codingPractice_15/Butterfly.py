#Butterfly 

n = int(input())

rows = 2*n 
cols = 2*n 

count = 2
count_2 = 2
for i in range(1,rows+1):
    if i ==1:
        hollow_spaces_upper = "  "*(rows - i -1)
        print("* "+hollow_spaces_upper+"* ")
    elif i == int((rows+1) / 2):
        stars = "* "*cols 
        print(stars)
        
    elif i == rows:
        hollow_spaces_upper = "  "*(rows - 2)
        print("* "+hollow_spaces_upper+"* ")
    else:
        if i > 1 and i < int((rows+1) / 2):
            
            hollow_spaces_upper = "  "*(rows - count -2)
            stars = "* "*i 
            stars_2 = "* "*i
            print(stars+hollow_spaces_upper+stars_2)
            count = count + 2
        elif i > int((rows+1) / 2) and i < rows:
            
            hollow_spaces_lower = "  "*(count_2-2 )
            stars = "* "*(rows+1 - i) 
            stars_2 = "* "*(rows+1 - i) 
            print(stars+hollow_spaces_lower+stars_2)
            count_2 = count_2 + 2
            
        