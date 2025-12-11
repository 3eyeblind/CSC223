from schedule import CourseSchedule


def print_menu() -> None:
    print("\nCourse Schedule System (BST vs AVL)")
    print("-----------------------------------")
    print("1. Display full schedule (BST)")
    print("2. Search by subject (BST)")
    print("3. Search by subject and catalog (BST)")
    print("4. Search by instructor last name (BST)")
    print("5. Show tree heights (BST vs AVL)")
    print("6. Quit")


def main():
    csv_file = "courses_2023.csv"

    # Build both schedules from the same CSV
    bst_schedule = CourseSchedule(backend="bst")
    avl_schedule = CourseSchedule(backend="avl")

    print("Loading course data from CSV...")
    bst_schedule.load_from_csv(csv_file)
    avl_schedule.load_from_csv(csv_file)

    print(f"Loaded {bst_schedule.record_count()} course entries into BST and AVL.")

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            items = bst_schedule.all_items()
            print("\nFull Schedule (BST, inorder by key):")
            print(bst_schedule.format_items(items))

        elif choice == "2":
            subject = input("Enter subject (e.g., CSC): ")
            items = bst_schedule.search_by_subject(subject)
            print(f"\nCourses with subject '{subject.upper()}' (BST):")
            print(bst_schedule.format_items(items))

        elif choice == "3":
            subject = input("Enter subject (e.g., CSC): ")
            catalog = input("Enter catalog number (e.g., 223): ")
            items = bst_schedule.search_by_subject_catalog(subject, catalog)
            print(f"\nCourses {subject.upper()} {catalog} (BST):")
            print(bst_schedule.format_items(items))

        elif choice == "4":
            last = input("Enter instructor last name: ")
            items = bst_schedule.search_by_instructor_last(last)
            print(f"\nCourses taught by '{last.title()}' (BST):")
            print(bst_schedule.format_items(items))

        elif choice == "5":
            bst_h = bst_schedule.tree_height()
            avl_h = avl_schedule.tree_height()
            print("\nTree Heights (after loading full CSV):")
            print(f"BST height: {bst_h}")
            print(f"AVL height: {avl_h}")
            if bst_h >= 0 and avl_h >= 0:
                diff = bst_h - avl_h
                if diff > 0:
                    print(f"AVL is shorter by {diff} edge(s), showing the effect of rotations/balancing.")
                elif diff == 0:
                    print("BST and AVL have the same height for this data set.")
                else:
                    print("Unexpected: AVL taller than BST for this data set (check implementation).")

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please enter 1–6.")


if __name__ == "__main__":
    main()