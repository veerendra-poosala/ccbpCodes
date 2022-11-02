#IdentifyTheMistakePattern

n = int(input())
for i in range(1, n+1):
    row_out = " " * (n-i)
    row_out = row_out + "$" * n
    print(row_out)
