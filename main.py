
#physics calculator program

print("Physics Calculator Menu")
print("1] Force")
print("2] Momentum")
print("3] Velocity")
print("4] Acceleration")
print("5] Exit")

choice = int(input("Choose [1/2/3/4/5]: "))

if choice == 1:
    mass = float(input("Enter Mass:"))
    acceleration = float(input("Enter Acceleration:"))
    force = mass * acceleration
    print(f"Force = {force}")

elif choice == 2:
    mass = float(input("Enter Mass:"))
    velocity = float(input("Enter Velocity:"))
    momentum = mass *velocity
    print(f"Momentum = {momentum}")

elif choice == 3:
    displacement = float(input("Enter Displacement:"))
    time = float(input("Enter Time:"))
    velocity = displacement * time
    print(f"Velocity = {velocity}")

elif choice == 4:
    initial_velocity = float(input("Enter Initial Velocity:"))
    final_velocity = float(input("Enter Final Velocity:"))
    time = float(input("Enter Time:"))
    acceleration = (final_velocity - initial_velocity) / time
    print(f"Acceleration = {acceleration}")

elif choice == 5:
    print("Thank you for using Physics Calculator Menu!")

else:
    Print("Invalid choice! Please choose a valid option. Thank you!")