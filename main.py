print("Welcome to PetPoint!")
print("Pet Grooming Appointment System")


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
            print("Adding a new appointment...")
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
