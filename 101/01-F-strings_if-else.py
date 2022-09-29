


def allowed_driving(name, age):
    if age >= 18:
        print(f"{name} is allowed to drive")
    elif age < 18: 
        print(f"{name} is not allowed to drive")
    else:
        pass

name = input("Name?: ")
MIN_DRIVING_AGE = int(input("age: ")) 

allowed_driving(name, MIN_DRIVING_AGE)