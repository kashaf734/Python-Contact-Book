import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book App")
        
        # Initialize contact list
        self.contacts = []
        
        # Create GUI elements
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.address_entry = tk.Entry(root, width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.search_label = tk.Label(root, text="Search by Name:")
        self.search_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
        self.search_entry = tk.Entry(root, width=20)
        self.search_entry.grid(row=6, column=1, padx=10, pady=10)
        
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=10)
        
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=8, column=0, columnspan=2, pady=10)
        
        self.delete_label = tk.Label(root, text="Delete by Name:")
        self.delete_label.grid(row=9, column=0, padx=10, pady=10, sticky=tk.W)
        self.delete_entry = tk.Entry(root, width=20)
        self.delete_entry.grid(row=9, column=1, padx=10, pady=10)
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=10, column=0, columnspan=2, pady=10)
        
        self.contact_listbox = tk.Listbox(root, width=50, height=10)
        self.contact_listbox.grid(row=11, column=0, columnspan=2, padx=10, pady=10)
        
        # Load contacts (if any) from file
        self.load_contacts()
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name:
            contact = {
                'name': name,
                'phone': phone,
                'email': email,
                'address': address
            }
            self.contacts.append(contact)
            self.contact_listbox.insert(tk.END, name)
            self.clear_entries()
            self.save_contacts()
            messagebox.showinfo("Info", "Contact added successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter a name for the contact.")
    
    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact['name'])
    
    def search_contact(self):
        query = self.search_entry.get()
        found = False
        self.contact_listbox.delete(0, tk.END)
        
        for contact in self.contacts:
            if query.lower() in contact['name'].lower():
                self.contact_listbox.insert(tk.END, contact['name'])
                found = True
        
        if not found:
            messagebox.showinfo("Info", f"No contacts found with name containing '{query}'.")
    
    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        
        if selected_index:
            index = selected_index[0]
            selected_contact = self.contacts[index]
            
            selected_contact['phone'] = self.phone_entry.get()
            selected_contact['email'] = self.email_entry.get()
            selected_contact['address'] = self.address_entry.get()
            
            self.contacts[index] = selected_contact
            self.save_contacts()
            messagebox.showinfo("Info", "Contact updated successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to update.")
    
    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.contact_listbox.delete(index)
            self.clear_entries()
            self.save_contacts()
            messagebox.showinfo("Info", "Contact deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
    
    def save_contacts(self):
        with open("contacts.txt", "w") as f:
            for contact in self.contacts:
                f.write(f"{contact['name']},{contact['phone']},{contact['email']},{contact['address']}\n")
    
    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as f:
                for line in f:
                    fields = line.strip().split(',')
                    contact = {
                        'name': fields[0],
                        'phone': fields[1],
                        'email': fields[2],
                        'address': fields[3]
                    }
                    self.contacts.append(contact)
        except FileNotFoundError:
            pass  # No saved contacts yet

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()