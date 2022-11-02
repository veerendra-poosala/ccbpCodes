#FourPassengersAndADriver

def number_of_cars_needed(no_of_people):
    required_cars = 0
    if no_of_people % 5 == 0:
        required_cars =int(no_of_people / 5)
    elif no_of_people % 5 != 0:
        total_cars = int(no_of_people/5)
        required_cars = int(total_cars)+1
    return required_cars


no_of_people = int(input())
result = number_of_cars_needed(no_of_people)
print(result)