import json
import os
import re

contacts_file='contacts.json'

def load_contacts():
    if not os.path.exists(contacts_file):
        return []
    with open(contacts_file,'r') as f:
        return json.load(f)

def save_contacts(contacts):
    with open(contacts_file,'w') as f:
        json.dump(contacts,f,indent=4)
        
def add_contact():
    name=input("Enter name: ").strip()
    phone=input("Enter phone number: ").strip()
    email=input("Enter email: ").strip()
    address=input("Enter address: ").strip()
    
    if not re.match(r'^\d{10}$',phone):
        print("Invalid phone number. Must be 10 digits.")
        return
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$',email):
        print("Invalid email format.")
        return
    
    contacts=load_contacts()
    contacts.append({"name":name,"phone":phone,"email":email,"address":address})
    confirm=input("Save contact? (y/n): ").strip().lower()
    if confirm=='y':
        save_contacts(contacts)
        print("Contact added successfully.")
    else:
        print("Contact not saved.")
        
def view_contacts():
    contacts=load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for index,contact in enumerate(contacts,start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")

def search_contact():
    search=input("Enter name or phone number to search: ").strip().lower()
    contacts=load_contacts()
    result=[c for c in  contacts if search in c['name'].lower() or search in c['phone']]
    if result:
        for contact in result:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
    else:
        print("No matching contact found")
        
def update_contact():
    name=input("Enter the name of the contact to update: ").strip().lower()
    contacts=load_contacts()
    for contact in contacts:
        if contact['name'].lower()==name:
            print("Leave field blank to keep current value.")
            new_name=input(f"New name ({contact['name']}): ").strip()
            new_phone=input(f"New phone ({contact['phone']}): ").strip()
            new_email=input(f"New email ({contact['email']}): ").strip()
            new_address=input(f"New address({contact['address']}): ").strip()
            
            if new_name:
                contact['name']=new_name
            if new_email:
                contact['email']=new_email
            if new_phone:
                contact['phone']=new_phone
            if new_address:
                contact['address']=new_address
                
            confirm=input("Save changes? (y/n): ").strip().lower()
            if confirm=='y':
                save_contacts(contacts)
                print("Changes saved successfully.")
                return
    print("Contact not found.")
    
def delete_contact():
    name=input("Enter the name of the contact to delete: ").strip().lower()
    contacts=load_contacts()
    updated=[c for c in contacts if c['name'].lower() != name]
    if len(updated)==len(contacts):
        print("Contact not found.")
    else:
        confirm=input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
        if confirm=='y':
            save_contacts(updated)
            print("Contact deleted.")
        else:
            print("Deletion cancelled.")
            return

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice=int(input("Select an option: "))
        
        if choice==1:
            add_contact()
        elif choice==2:
            view_contacts()
        elif choice==3:
            search_contact()
        elif choice==4:
            update_contact()
        elif choice==5:
            delete_contact()
        elif choice==6:
            print("Session ended. Your contacts are safe!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__=="__main__":
    main()