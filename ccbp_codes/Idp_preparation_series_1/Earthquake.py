#Earthquake

def main():
    magnitude_a,magnitude_b = map(int,input().split())
    difference = magnitude_a - magnitude_b 
    power = 32 ** difference
    print(power)
main()