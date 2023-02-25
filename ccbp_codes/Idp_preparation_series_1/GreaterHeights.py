#GreaterHeights

def get_answer_to_the_query(heights_of_students_list,each_query):
    answers= 0
    for height in heights_of_students_list:
        if each_query <= height:
            answers += 1 
    return answers

def answer_the_queries(heights_of_students_list,queries_list):
    for each_query in queries_list:
        answer =  get_answer_to_the_query(heights_of_students_list,each_query)
        print(answer)
    

def get_queries_list(n):
    queries_list = []
    for i in range(n):
        item = int(input())
        queries_list.append(item)
    return queries_list
    

def main():
    n_of_students,n_of_queries = map(int,input().split())
    #print(n_of_queries,n_of_students)
    heights_of_students_list = list(map(int,input().split()))
    #print(heights_of_students_list)
    queries_list = get_queries_list(n_of_queries)
    #print(queries_list)
    answer_the_queries(heights_of_students_list,queries_list)

main()
    