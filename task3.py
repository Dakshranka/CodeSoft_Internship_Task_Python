class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact
        print("Contact updated successfully.")

    def delete_contact(self, index):
        del self.contacts[index]
        print("Contact deleted successfully.")

def display_menu():
    print("\nContact Manager Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contact_manager = ContactManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_manager.search_contact(keyword)
            if found_contacts:
                print("Search Results:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == "4":
            index = int(input("Enter index of contact to update: ")) - 1
            if 0 <= index < len(contact_manager.contacts):
                name = input("Enter new name: ")
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                updated_contact = Contact(name, phone_number, email, address)
                contact_manager.update_contact(index, updated_contact)
            else:
                print("Invalid index.")
        elif choice == "5":
            index = int(input("Enter index of contact to delete: ")) - 1
            if 0 <= index < len(contact_manager.contacts):
                contact_manager.delete_contact(index)
            else:
                print("Invalid index.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
