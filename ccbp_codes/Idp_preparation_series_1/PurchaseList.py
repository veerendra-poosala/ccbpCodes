#PurchaseList

def get_item_sold_by_once(purchases_list):
    count = 1
    result = None
    for item in purchases_list:
        c = purchases_list.count(item)
        if c == count:
            result = item
            return result
    return result
def get_item_sold_more_than_once(purchases_list):
    count = 1
    result = None
    for item in purchases_list:
        c = purchases_list.count(item)
        if c > count:
            result = item
            return result
    return result

def main():
    purchases_list = list(map(int,input().split()))
    item_sold_by_once = get_item_sold_by_once(purchases_list)
    item_sold_more_than_once = get_item_sold_more_than_once(purchases_list)
    print(item_sold_by_once)
    print(item_sold_more_than_once)
main()