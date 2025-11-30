appointments = []


print("Welcome to PetPoint!")
print("Pet Grooming Appointment System")

def add_appointment():
    print("\n--- Add New Appointment ---")
    pet_name = input("Pet name: ")
    owner_name = input("Owner name: ")
    date = input("Appointment date (e.g., 2025-12-01): ")
    time = input("Appointment time (e.g., 2:30 PM): ")
    service = input("Service type (e.g., bath, grooming, nail trim): ")

    appointment = {
        "pet_name": pet_name,
        "owner_name": owner_name,
        "date": date,
        "time": time,
        "service": service
    }

    appointments.append(appointment)
    print("\nAppointment added successfully!")
    print(f"- {pet_name} ({owner_name}) on {date} at {time} for {service}")

def show_menu():
    print("\n===== PetPoint Menu =====")
    print("1. Add new appointment")
    print("2. View appointments")
    print("3. Search appointments")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_appointment()

        elif choice == "2":
            print("Viewing appointments...")
        elif choice == "3":
            print("Searching appointments...")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

main()
