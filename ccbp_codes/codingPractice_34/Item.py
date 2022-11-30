#Item
# Item class should have the following attributes & methods
#
# Attributes:
#   name, price, category
#
# Methods:
#   get_detail: Print the details of the item in the format '{name}@{price}-{category}'
#
# If the value of price is less than 1, raise ValueError exception like
#   "ValueError: Invalid value for price, got {price}"


# Implement the Item class appropriately
class Item:
    def __init__(self, name, price, category):
        if price < 1:
            raise ValueError ("Invalid value for price, got {}".format(price))   
        self.name = name
        self.price = price 
        self.category = category
     
        

    def get_detail(self):
        return "{}@{}-{}".format(self.name,self.price,self.category)
        
             
   

# You need not change any code below.
# Do not call this function anywhere. It will automatically be called internally during tests.
def default_test():
    item = Item(name="Oreo Biscuits", price=30, category="Food")
    print(item.name)  # prints "Oreo Biscuits"
    print(item.price)  # prints '30'
    print(item.category)  # prints "Food"
    print(item.get_detail())  # prints "Oreo Biscuits@30-Food"
   
