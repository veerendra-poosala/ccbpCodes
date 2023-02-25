#NGreatestNumbers


list_a = [5, 20, 3, 7, 6, 8]
list_a.sort() #sorting list
k = int(input())
list_len = len(list_a)
res = list_a[list_len - k:] 
for i in range(k):
    res[i] = str(res[i]) #updating res list
print(" ".join(res)) #converting into a string
