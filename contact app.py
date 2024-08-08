import tkinter as tk
from tkinter import messagebox, simpledialog, font

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biswajit Contact App")
        self.root.geometry("600x600")  
        self.root.resizable(True, True)  

        self.background_color = "#E6E6FA"  
        self.header_color = "#6A5ACD"  
        self.button_color = "#28a745"  
        self.button_hover_color = "#218838"  
        self.text_color = "#343a40"  
        self.footer_color = "#4B0082"  

        self.title_font = font.Font(family="Helvetica", size=22, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=12)

        self.canvas = tk.Canvas(root, bg=self.background_color)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.frame_header = tk.Frame(self.canvas, bg=self.header_color)
        self.frame_header.pack(fill=tk.X, pady=(10, 0))

        self.frame_main = tk.Frame(self.canvas, bg=self.background_color)
        self.frame_main.pack(pady=20, fill=tk.BOTH, expand=True)

        self.frame_footer = tk.Frame(self.canvas, bg=self.footer_color)
        self.frame_footer.pack(side=tk.BOTTOM, fill=tk.X, pady=(0, 10))

        self.contacts = []

        self.create_widgets()
        
    def create_widgets(self):
        self.header_label = tk.Label(self.frame_header, text="Biswajit Contact App", font=self.title_font, bg=self.header_color, fg="white")
        self.header_label.pack(pady=15)

        self.frame_inputs = tk.Frame(self.frame_main, bg=self.background_color)
        self.frame_inputs.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.label_name = tk.Label(self.frame_inputs, text="Name:", font=self.label_font, bg=self.background_color, fg=self.text_color)
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.entry_name = tk.Entry(self.frame_inputs, font=self.label_font, width=40)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        self.label_phone = tk.Label(self.frame_inputs, text="Phone:", font=self.label_font, bg=self.background_color, fg=self.text_color)
        self.label_phone.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.entry_phone = tk.Entry(self.frame_inputs, font=self.label_font, width=40)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        self.label_email = tk.Label(self.frame_inputs, text="Email:", font=self.label_font, bg=self.background_color, fg=self.text_color)
        self.label_email.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.entry_email = tk.Entry(self.frame_inputs, font=self.label_font, width=40)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

        self.label_address = tk.Label(self.frame_inputs, text="Address:", font=self.label_font, bg=self.background_color, fg=self.text_color)
        self.label_address.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.entry_address = tk.Entry(self.frame_inputs, font=self.label_font, width=40)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

        self.frame_inputs.grid_columnconfigure(1, weight=1)

        self.frame_buttons = tk.Frame(self.frame_main, bg=self.background_color)
        self.frame_buttons.pack(pady=10, fill=tk.X)

        self.button_width = 20
        self.button_height = 2

        self.btn_add = self.create_button("Add Contact", self.add_contact)
        self.btn_view = self.create_button("View Contacts", self.view_contacts)
        self.btn_search = self.create_button("Search Contacts", self.search_contact)
        self.btn_update = self.create_button("Update Contact", self.update_contact)
        self.btn_delete = self.create_button("Delete Contact", self.delete_contact)

        self.btn_add.pack(side=tk.TOP, padx=10, pady=5)
        self.btn_view.pack(side=tk.TOP, padx=10, pady=5)
        self.btn_search.pack(side=tk.TOP, padx=10, pady=5)
        self.btn_update.pack(side=tk.TOP, padx=10, pady=5)
        self.btn_delete.pack(side=tk.TOP, padx=10, pady=5)

        self.contacts_display = tk.Text(self.frame_main, font=self.label_font, height=10, width=80, bg=self.background_color, fg=self.text_color, wrap=tk.WORD)
        self.contacts_display.pack(pady=10)
        self.contacts_display.config(state=tk.DISABLED)

        self.footer_label = tk.Label(self.frame_footer, text="📞 &copy; 2024 All Rights Reserved", font=self.label_font, bg=self.footer_color, fg="white")
        self.footer_label.pack(pady=(10, 0))

        self.footer_line = tk.Frame(self.frame_footer, bg="white", height=2)
        self.footer_line.pack(fill=tk.X, pady=(0, 5))
        
    def create_button(self, text, command):
        button = tk.Button(self.frame_buttons, text=text, command=command, font=self.button_font, bg=self.button_color, fg="white", width=self.button_width, height=self.button_height, relief="raised", borderwidth=2)
        button.bind("<Enter>", lambda e: button.config(bg=self.button_hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=self.button_color))
        return button

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        
        if name and phone and email and address:
            self.contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
            self.clear_input_fields()
            self.update_contacts_display()
            messagebox.showinfo("Success", "Contact added successfully!", parent=self.root)
        else:
            messagebox.showwarning("Input Error", "All fields are required.", parent=self.root)

    def clear_input_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

    def update_contacts_display(self):
        self.contacts_display.config(state=tk.NORMAL)
        self.contacts_display.delete(1.0, tk.END)  
        if self.contacts:
            for contact in self.contacts:
                contact_info = f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}\n"
                self.contacts_display.insert(tk.END, contact_info)
        else:
            self.contacts_display.insert(tk.END, "No contacts available.\n")
        self.contacts_display.config(state=tk.DISABLED)

    def view_contacts(self):
        top = tk.Toplevel()
        top.title("Contact List")
        top.geometry("500x400")
        top.config(bg=self.background_color)
        
        tk.Label(top, text="Contact List", font=self.title_font, bg=self.background_color, fg=self.text_color).pack(pady=10)
        
        if not self.contacts:
            tk.Label(top, text="No contacts available.", font=self.label_font, bg=self.background_color, fg=self.text_color).pack(pady=10)
        else:
            contact_frame = tk.Frame(top, bg=self.background_color)
            contact_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
            
            for contact in self.contacts:
                contact_info = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"
                tk.Label(contact_frame, text=contact_info, font=self.label_font, bg=self.background_color, fg=self.text_color, justify=tk.LEFT).pack(pady=5)

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name or phone number:", parent=self.root)
        
        if query:
            results = [contact for contact in self.contacts if query in contact['name'] or query in contact['phone']]
            
            if results:
                result_text = "\n\n".join([f"Name: {contact['name']}\nPhone: {contact['phone']}" for contact in results])
                messagebox.showinfo("Search Results", result_text, parent=self.root)
            else:
                messagebox.showinfo("Search Results", "No contacts found.", parent=self.root)
        else:
            messagebox.showwarning("Input Error", "Search query cannot be empty.", parent=self.root)

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:", parent=self.root)
        if name:
            for contact in self.contacts:
                if contact['name'] == name:
                    new_name = simpledialog.askstring("Update Contact", "Enter new name (leave blank to keep unchanged):", initialvalue=contact['name'], parent=self.root)
                    new_phone = simpledialog.askstring("Update Contact", "Enter new phone (leave blank to keep unchanged):", initialvalue=contact['phone'], parent=self.root)
                    new_email = simpledialog.askstring("Update Contact", "Enter new email (leave blank to keep unchanged):", initialvalue=contact['email'], parent=self.root)
                    new_address = simpledialog.askstring("Update Contact", "Enter new address (leave blank to keep unchanged):", initialvalue=contact['address'], parent=self.root)
                    
                    if new_name:
                        contact['name'] = new_name
                    if new_phone:
                        contact['phone'] = new_phone
                    if new_email:
                        contact['email'] = new_email
                    if new_address:
                        contact['address'] = new_address
                    
                    self.update_contacts_display()
                    messagebox.showinfo("Success", "Contact updated successfully!", parent=self.root)
                    return
            messagebox.showwarning("Update Error", "Contact not found.", parent=self.root)
        else:
            messagebox.showwarning("Input Error", "Name cannot be empty.", parent=self.root)

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:", parent=self.root)
        if name:
            for contact in self.contacts:
                if contact['name'] == name:
                    self.contacts.remove(contact)
                    self.update_contacts_display()
                    messagebox.showinfo("Success", "Contact deleted successfully!", parent=self.root)
                    return
            messagebox.showwarning("Delete Error", "Contact not found.", parent=self.root)
        else:
            messagebox.showwarning("Input Error", "Name cannot be empty.", parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
