from schedule import Schedule


def display_menu() -> None:
    
    print("\nCourse Schedule System")
    print("----------------------")
    print("1. Display full schedule")
    print("2. Search by subject")
    print("3. Search by subject and catalog number")
    print("4. Search by instructor last name")
    print("5. Quit")


def main() -> None:
    schedule = Schedule()

    csv_filename = "courses.csv"

    print(f"Loading course data from '{csv_filename}' ...")
    try:
        schedule.load_from_csv(csv_filename)
    except FileNotFoundError:
        print(f"ERROR: Could not find '{csv_filename}'.")
        print("Make sure the CSV file is in the same folder as main.py.")
        return

    print(f"Loaded {len(schedule)} course entries.\n")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            # Display full schedule
            print("\nFull Course Schedule")
            print("--------------------")
            if len(schedule) == 0:
                print("No course data loaded.")
            else:
                schedule.print()

        elif choice == "2":
            # Search by subject
            subject = input("Enter subject (e.g., BIO, MTH, CSC): ").strip()
            results = schedule.find_by_subject(subject)

            print(f"\nCourses with subject '{subject.upper()}':")
            print("---------------------------------------")
            if not results:
                print("No courses found.")
            else:
                schedule.print(results)

        elif choice == "3":
            # Search by subject + catalog
            subject = input("Enter subject (e.g., BIO): ").strip()
            catalog = input("Enter catalog number (e.g., 142): ").strip()
            results = schedule.find_by_subject_catalog(subject, catalog)

            print(f"\nCourses with subject '{subject.upper()}' and catalog '{catalog}':")
            print("-------------------------------------------------------------")
            if not results:
                print("No courses found.")
            else:
                schedule.print(results)

        elif choice == "4":
            # Search by instructor last name
            last_name = input("Enter instructor last name (e.g., Abrahams): ").strip()
            results = schedule.find_by_instructor_last_name(last_name)

            print(f"\nCourses taught by instructor with last name '{last_name}':")
            print("--------------------------------------------------------")
            if not results:
                print("No courses found.")
            else:
                schedule.print(results)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()