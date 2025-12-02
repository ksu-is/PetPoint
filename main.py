appointments = []

print("Welcome to PetPoint!")
print("Pet Grooming Appointment System")


def show_menu():
    print("\n===== PetPoint Menu =====")
    print("1. Add new appointment")
    print("2. View appointments")
    print("3. Search appointments")
    print("4. Exit")


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


def view_appointments():
    print("\n--- All Appointments ---")

    if not appointments:
        print("No appointments scheduled yet.")
        return

    for index, appt in enumerate(appointments, start=1):
        print(
            f"{index}. {appt['pet_name']} ({appt['owner_name']}) - "
            f"{appt['date']} at {appt['time']} for {appt['service']}"
        )


def search_appointments():
    print("\n--- Search Appointments ---")

    if not appointments:
        print("No appointments to search yet.")
        return

    term = input("Enter pet name or owner name to search: ").strip().lower()

    matches = []
    for appt in appointments:
        pet = appt["pet_name"].lower()
        owner = appt["owner_name"].lower()
        if term in pet or term in owner:
            matches.append(appt)

    if not matches:
        print(f"No appointments found matching '{term}'.")
    else:
        print(f"\nResults for '{term}':")
        for index, appt in enumerate(matches, start=1):
            print(
                f"{index}. {appt['pet_name']} ({appt['owner_name']}) - "
                f"{appt['date']} at {appt['time']} for {appt['service']}"
            )


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            search_appointments()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


main()
