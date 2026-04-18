import json

FILE_NAME = "contact.json"

def load_contacts():
    try: 
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f)

def is_valid_phone(phone):
    return phone.isdigit()

def add_contact(contacts):
    name = input("Please enter your name: ").title()
    if name in contacts:
        print("Contact already exists.")
        return
    
    phone = input("Enter phone number: ")
    if not is_valid_phone(phone):
        print("Phone number must contain digits only.")
        return

    contacts[name] = phone 
    save_contacts(contacts) 
    print(f"Saved! {name} → {phone}")


def view_contacts(contacts):
    if not contacts: 
        print("Empty Contact Book")
        return
                
    for name, phone in contacts.items(): 
        print(f"Name: {name} | Phone: {phone}")

def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").title()

    if name not in contacts:
        print("No such name exists in the Contact file.")
        return

    phone = input("Enter new phone number: ")

    if not is_valid_phone(phone):
        print("Phone number must contain digits only.")
        return
    
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Contact updated! {name} → {phone}")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").title() 
    if name not in contacts:
        print("Contact not found!")
        return

    del contacts[name]
    print(f"{name} is deleted on the contact file")
    save_contacts(contacts)

def search_contact(contacts):
    query = input("Who's you want to search?: ").strip().lower()

    matches = {
        name: phone
        for name, phone in contacts.items()
        if query in name.lower()
    }

    if matches:
        print("\nMatches found:")
        for name, phone in matches.items():
            print(f"{name}: {phone}")
    else:
        print("No matching contacts found.")

def show_menu():
     print("""
Choose an action:
- add
- view
- edit
- delete
- search
- exit
""")

def contact_book():
    contacts = load_contacts()

    actions = {
        "add": add_contact,
        "view": view_contacts,
        "edit": edit_contact,
        "delete": delete_contact,
        "search": search_contact,
    }

    while True:
        show_menu()
        choice = input("Your choice: ").lower()

        if choice == "exit":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action(contacts)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    contact_book()


# Older Version
# def contact_book(contacts):
    
# #     while True:
# #         print("""
# #         Type "add": if you want to create a new contact file
# #         Type "view": if you want to view the contact file
# #         Type "edit": if you want to edit a contact file
# #         Type "delete: if you want to delete a contact file
# #         Type "exit": if you want to exit the contact file
# #         Type "search": if you want to search someone in contact file
# #         """)


# #         user_input = input("What is your action?: ").lower()


# #         if user_input == "add":

            
# #             name = input("Please enter your name: ").title() 
# #             phone = input("Please enter your phone number: ") 
            
# #             if name in contact_file:
# #                 print("Existing contact name!")
# #             else:
# #                 if phone.isdigit():
# #                     contacts[name] = phone 
# #                     save_contacts(contacts) 
# #                     print(f"Contact Saved! {name} and {phone} added!")
# #                 else:
# #                     print("Phone number must have numbers only!") 


# #         elif user_input == "view":
# #                 if not contact_file: 
# #                     print("Empty Contact Book")
# #                 else:
# #                     for name, phone in contact_file.items(): 
# #                         print(f"Name: {name} | Phone: {phone}")


# #         elif user_input == "edit":
# #             contact_name = input("Enter the name of the contact to edit: ").title()
# #             if contact_name in contact_file:
# #                 new_phone = input(f"Enter new phone number for {contact_name}: ")
# #                 if new_phone.isdigit():
# #                     contacts[contact_name] = new_phone
# #                     save_contacts(contacts)
# #                     print(f"Contact updated! {contact_name} → {new_phone}")
# #                 else:
# #                     print("Phone number must have numbers only!")
# #             else:
# #                 print("No such name exists in the Contact file.")


# #         elif user_input == "delete":
# #             contact_name = input("Who's you want to remove?: ").title() 
# #             if contact_name in contact_file: 
# #                 del contacts[contact_name]
# #                 print(f"{contact_name} is deleted on the contact file")
# #                 save_contacts(contacts)
# #             else:
# #                 print("No such name exist on the Contact file")


# #         elif user_input == "exit":
# #             print("Exiting the contact book...")
# #             break
# #         elif user_input == "search":
# #             search_input = input("Search contact: ")

# #             if search_input in contact_file:
# #                 print(f"{search_input} exists on the contact file")
# #             else:
# #                 print(f"{search_input} doesn't exists on the contact file")
# #         else:
# #             print("Invalid action...")
# contact_book(contact_file)
