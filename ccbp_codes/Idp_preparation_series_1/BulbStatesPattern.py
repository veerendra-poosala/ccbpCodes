#BulbStatesPattern
def get_visits_summary_list(n):
    visits_summary_list = []
    for i in range(1,n+1):
        visit = list(range(1,n+1))
        light_status_list = []
        if i % 2 ==1:
            for num in visit:
                if num % 2 == 0:
                    light_status_list.append(0)
                elif num %2 ==1:
                    light_status_list.append(1)
        elif i % 2 == 0:
            for num in visit:
                if num % 2 == 0:
                    light_status_list.append(1)
                elif num %2 ==1:
                    light_status_list.append(0)
        visits_summary_list.append(light_status_list)
    return visits_summary_list

def print_summary(visits_summary_list):
    for visit in visits_summary_list:
        result = ""
        for item in visit:
            item = str(item)
            result += item + " "
        print(result)
        


def main():
    n = int(input())
    visits_summary_list = get_visits_summary_list(n)
    print_summary(visits_summary_list)
main()
    