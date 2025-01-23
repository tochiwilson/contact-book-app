from contact import Contact
from rapidfuzz import process

# 1. Contact Book Application

# Description:
# Create an application to manage basic contact information,
# including first name, last name, and phone number.
# Users can add, edit, delete, and search contacts.
# The data is stored in a file (CSV) to ensure it is preserved even after the application is closed.

# Challenge:
# Add a search feature with fuzzy matching.
# Use the fuzzywuzzy or RapidFuzz library to search for names,
# even if the user makes a typo. For example, "Jon" should match "John."


contacts: list[Contact] = []

def main():
    load_contacts()

    while True:
        print("\n1. Add contact")
        print("2. Get all contacts")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6 Exit")

        choice = int(input())

        match choice:
            case 1:
                create_contact()
            case 2:
                get_all_contacts()
            case 3:
                search_contact()
                search_contact_with_fuzz()
            case 4:
                edit_contact()
            case 5:
                delete_contact()
            case _:
                break


def load_contacts():
    with open("contact_list.csv", "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            first_name, last_name, phone_number = stripped_line.split(",")
            line_contacts = Contact(
                first_name=first_name, last_name=last_name, phone_number=phone_number
            )

            contacts.append(line_contacts)


def create_contact():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone_number = input("Phone number: ")

    new_contact = Contact(first_name, last_name, phone_number)
    print("Contact created")

    with open("contact_list.csv", "+a") as f:
        f.write(f"{new_contact.first_name},{new_contact.last_name},{new_contact.phone_number}\n")

    contacts.append(new_contact)


def get_all_contacts():
    print("All the contacts:")
    for contact in contacts:
        print(contact)


def search_contact():
    query = input("Enter the name to search: ").lower()
    results = [contact for contact in contacts if query in f"{contact.first_name} {contact.last_name}".lower()]

    if results:
        print("\nSearch results:")
        for contact in results:
            print(contact)
    else:
        print("No contacts found matching your query.")


def search_contact_with_fuzz():
    search_name = input("Enter the name to search: ").lower()
    contact_names = [f"{c.first_name} {c.last_name}".lower() for c in contacts]

    matches = process.extract(search_name, contact_names)

    if matches:
        print("\nFound contacts:")
        for match in matches:
            name, score, index = match
            if score > 65:
                print(f"- {contacts[index]}")
    else:
        print("No contacts found")


def edit_contact():
    name = input("Give the name of the contact you want to edit ").lower()
    found_contacts = [c for c in contacts if name in f"{c.first_name} {c.last_name}".lower()]

    if not found_contacts:
        print("No contact found with that name")
        return

    print("Contact found")
    for idx, contact in enumerate(found_contacts):
        print(f"{idx + 1}. {contact}")

    choice = int(input("Select the number of the contact to edit: ")) - 1
    if 0 <= choice < len(found_contacts):
        contact = found_contacts[choice]
        print(f"Editing contact: {contact}")

        contact.first_name = input("New first name (leave blank to keep current): ") or contact.first_name
        contact.last_name = input("New last name (leave blank to keep current): ") or contact.last_name
        contact.phone_number = input("New phone number (leave blank to keep current): ") or contact.phone_number

        print("Contact updated!")
        save_contacts()
    else:
        print("Invalid choice.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    found_contacts = [c for c in contacts if name.lower() in f"{c.first_name} {c.last_name}".lower()]

    if not found_contacts:
        print("No contact found with that name.")
        return

    print("Contacts found:")
    for idx, contact in enumerate(found_contacts):
        print(f"{idx + 1}. {contact}")

    choice = int(input("Select the number of the contact to delete: ")) - 1
    if 0 <= choice < len(found_contacts):
        contact = found_contacts.pop(choice)
        contacts.remove(contact)
        print(f"Deleted contact: {contact}")
        save_contacts()
    else:
        print("Invalid choice.")


def save_contacts():
    with open("contact_list.csv", "w") as f:
        for contact in contacts:
            f.write(f"{contact.first_name},{contact.last_name},{contact.phone_number}\n")


if __name__ == "__main__":
    main()

