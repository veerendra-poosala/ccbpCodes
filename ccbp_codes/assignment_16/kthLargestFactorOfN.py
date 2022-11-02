#kthLargestFactorOfN

given_number_n = int(input())
k = int(input())  #kthLargestFactorOfN

factor = given_number_n

counter = 0
for i in range(1,given_number_n+1):
    if given_number_n % factor  == 0:
        counter = counter+1
        #print("factor",factor)
        #print("count",counter)
        if counter == k:
            print(factor)
            break
    factor = factor - 1

if counter < k:
    print(1)
