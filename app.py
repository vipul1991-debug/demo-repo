import math
print("Enter velocity : ")
input_velocity = float(input())
print("Enter angle : ")
input_angle = float(input())


def calculate_distance(velocity, angle):
    distance = (velocity ** 2) * math.sin(2 * math.radians(angle)) / 9.8
    return distance


print("The distance traveled by the projectile is : ",
      calculate_distance(input_velocity, input_angle))
