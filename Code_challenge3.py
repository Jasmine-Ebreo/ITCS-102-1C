
name = input("Enter your name ---->")

fare = float(input("How much is your fare --->"))
student = input("Are you a Student (Yes/No)?")


if student.lower() == 'yes':
    disc = 0.20
    disc_amoount = fare * disc
    disc_fare = fare - disc_amoount
    print(f"\nHello, {name}")
    print(f"The original fare is: ₱{fare:.2f}")
    print(f"The student discount amount is: ₱{disc_amoount:.2f}")
    print(f"The discounted fare is: ₱{ disc_fare:.2f}")
    
else:
    print(f"\nHello, {name}")
    print(f"You are not eligible for a student discount.")
    print(f"The regular fare is: ₱{fare:.2f}")

print("\nThank you for using my program")

