
def add_contact(contact_book, name, phone, email):
    contact_book[name] = {'phone': phone, 'email': email}
    print(f"Contact Added: {name}")

def find_contact(contact_book, name):
    if name in contact_book:
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
    else:
        print("Contact not found for {name}")

def delete_contact(contact_book, name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact Deleted {name}")
    else:
        print("Contact not found for {name}")

def display_all_contacts(contact_book):
    if contact_book:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print("-" * 20)
    else:
        print("No contacts in the contact book")

def main():
    contact_book = {}
    while True:
        print("Contact Book Menu: ")
        print("1. Add Contact ")
        print("2. Find Contact ")
        print("3. Delete Contact ")
        print("4. Display all Contacts ")
        print("5. Exit ")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            add_contact(contact_book, name, phone, email)
        elif choice == '2':
            name = input("Enter Name: ")
            find_contact(contact_book, name)
        elif choice == '3':
            name = input("Enter Name: ")
            delete_contact(contact_book, name)
        elif choice == '4':
            display_all_contacts(contact_book)
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
