import json
import os

CONTACT_FILES='contact.json'

def load_contacts():
    if not os.path.exists(CONTACT_FILES):
        return []
    try:
        with open(CONTACT_FILES,'r') as file:
            return json.load(file)
    except (json.JSONDecodeError,FileNotFoundError):
        return []
    
def save_contacts(contacts):
    with open(CONTACT_FILES,'w') as file:
        json.dump(contacts,file,indent=4)

def add_contacts(contacts):
    name=input('Enter contact name:')
    email=input('Enter email address:')
    phone=int(input('Enter phone number:'))
    contacts.append({'name':name,'phone':phone,'email':email})
    save_contacts(contacts)
    print('Contact added Successfully')

def view_contacts(contacts):
    if not contacts:
        print('No contact found')
    else:
        for index,contact in enumerate(contacts,start=1):
            print(f'{index} Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}')

def edit_contacts(contacts):
    view_contacts(contacts)
    try:
        index=int(input('Enter the number of contact you want to edit')) - 1
        if 0 <= index < len(contacts):
            contacts[index]['name']=input("Enter new contact name:")
            contacts[index]['phone']=int(input('Enter new phone number:'))
            contacts[index]['email']=input('Enter new email address')
            save_contacts(contacts)
            print('Contact updated successfully')
        else:
            print('Invalid contact number')
    except ValueError:
        print('Invalid input. Please enter a valid number.')

def delete_contacts(contacts):
    view_contacts(contacts)
    try:
        index=int(input('Enter a contact number you want to delete')) - 1
        if 0 <= index < len(contacts):
            contacts.pop(index)
            save_contacts(contacts)
            print('Contact deleted successfully')
        else:
            print('Invalid contact number')
    except ValueError:
        print('Invalid input. Please enter a valid number. ')

def main():
    contacts=load_contacts()

    while True:
        print('\nContact Management System')
        print('1. Add a new contact')
        print('2. View contacts')
        print('3. Edit a contacts')
        print('4. Delete a contact')
        print('5. Exit')

        choice=input('Enter your choice:')

        if choice =='1':
            add_contacts(contacts)
        elif choice =='2':
            view_contacts(contacts)
        elif choice =='3':
            edit_contacts(contacts)
        elif choice =='4':
            delete_contacts(contacts)
        elif choice =='5':
            print('Good Bye!')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()