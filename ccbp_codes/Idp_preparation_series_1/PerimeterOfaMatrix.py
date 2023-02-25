#PerimeterOfaMatrix
def get_matrix(m,n):
    new_matrix = []
    for i in range(m):
        row = []
        item = list(map(int,input().split()))
        new_matrix.append(item)
    return new_matrix

def get_perimeter_of_matrix(matrix):
    length = len(matrix)
    total = 0
    for i in range(length):
        row_total = 0
        for j in range(len(matrix[i])):
            if i == 0 or i == (length-1):
                item = matrix[i][j]
                row_total += item
            else:
                if j == 0 or j == (len(matrix[i]) -1):
                    item = matrix[i][j]
                    row_total += item
        total += row_total
    return total

    
m,n = map(int,input().split())

matrix = get_matrix(m,n)
#print(matrix)
perimeter = get_perimeter_of_matrix(matrix)
print(perimeter)