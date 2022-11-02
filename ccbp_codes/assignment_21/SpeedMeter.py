#SpeedMeter

def get_speed_status(speed):
    if speed < 60:
        return "Normal"
    elif speed >= 60 and speed < 80:
        return "Warning"
    elif speed >= 80:
        return "Over Speed"


speed = int(input())
result = get_speed_status(speed)
print(result)
