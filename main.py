# Campus Navigation System
# Beginner-friendly project - uses only basic Python (no external modules).

import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "campus_data.txt")


def read_data():
    locations = []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines[1:]:
        values = line.strip().split("|")
        if len(values) == 6:
            location = {
                "id": int(values[0]),
                "parent_id": int(values[1]),
                "type": values[2],
                "name": values[3],
                "category": values[4],
                "description": values[5]
            }
            locations.append(location)

    return locations


def get_path(location, locations):
    path = [location["name"]]
    parent_id = location["parent_id"]

    while parent_id != 0:
        parent = None
        for item in locations:
            if item["id"] == parent_id:
                parent = item
                break

        if parent is None:
            break

        path.insert(0, parent["name"])
        parent_id = parent["parent_id"]

    return " > ".join(path)


def show_locations(results, locations):
    if len(results) == 0:
        print("\nNo matching information found.")
        return

    for item in results:
        print("\n--------------------------------")
        print("Name:", item["name"])
        print("Type:", item["type"])
        print("Category:", item["category"])
        print("Located at:", get_path(item, locations))
        print("Information:", item["description"])


def search_location(locations):
    keyword = input("\nEnter a name, type, category or keyword: ").lower().strip()
    results = []

    for item in locations:
        details = (item["name"] + " " + item["type"] + " " +
                   item["category"] + " " + item["description"]).lower()

        if keyword in details:
            results.append(item)

    show_locations(results, locations)


def explore_category(locations):
    categories = []

    for item in locations:
        if item["category"] not in categories:
            categories.append(item["category"])

    print("\nCAMPUS CATEGORIES")
    for number, category in enumerate(categories, 1):
        print(str(number) + ".", category)

    try:
        choice = int(input("Choose a category number: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if choice < 1 or choice > len(categories):
        print("Invalid choice.")
        return

    selected = categories[choice - 1]
    results = []

    for item in locations:
        if item["category"] == selected:
            results.append(item)

    show_locations(results, locations)


def main():
    locations = read_data()

    while True:
        print("\n========== CAMPUS NAVIGATION SYSTEM ==========")
        print("1. Search campus information")
        print("2. Explore by category")
        print("3. View all campus locations")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search_location(locations)
        elif choice == "2":
            explore_category(locations)
        elif choice == "3":
            show_locations(locations, locations)
        elif choice == "4":
            print("Thank you for using Campus Navigation System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
