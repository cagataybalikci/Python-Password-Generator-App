from tkinter import messagebox
from tkinter import *
import password_generator
import pyperclip
import json

# CONSTANTS
DARK = "#383e56"
ORANGE = "#fb743e"


# PASS WORD GENERATOR

def generate_password():
    gen_password = password_generator.random_password()
    password_input.insert(0, gen_password)
    pyperclip.copy(gen_password)
    messagebox.showinfo(title="Password Generated!",
                        message="Secure password generated and copy to clipboard for your use. ")


# SAVE PASSWORD

def add():
    website_name = website_input.get().title()
    email = email_input.get()
    password = password_input.get()
    new_data = {website_name: {
        "email": email,
        "password": password,
    }}

    if len(website_name) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Space", message="You need to fill all boxes.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, "end")
            password_input.delete(0, "end")


def search():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            website_name = website_input.get().title()
            if len(website_name) != 0:
                if website_name in data:
                    email = data[website_name]["email"]
                    password = data[website_name]["password"]
                    messagebox.showinfo(title=website_name,
                                        message=f"Website Name: {website_name}\nEmail : {email}\n "
                                                f"Password : {password}")
                else:
                    messagebox.showerror(title="Not Found!!!",
                                         message=f"No password found related to {website_name}!!!")

            else:
                messagebox.showerror(title="Empty Input Area!!!",
                                     message="You need to type something to search...")
    except FileNotFoundError:
        messagebox.showerror(title="No data file found!!",
                             message="You need to create at least one password to create data "
                                     "file to use search function...")


# UI SETUP
window = Tk()
window.title("Password Manager")

# App Icon
img = Image("photo", file="images/logo.png")
window.call('wm', 'iconphoto', window.w, img)

# Screen setup
window.maxsize(width=500, height=500)
window.minsize(width=500, height=500)
window.config(bg=DARK, padx=20, pady=20)
canvas = Canvas(width=200, height=200, bg=DARK, highlightthickness=0)
bg_image = PhotoImage(file="images/logo.png")
canvas.create_image(128, 128, image=bg_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website Name:", bg=DARK, fg=ORANGE, pady=10)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg=DARK, fg=ORANGE, pady=10)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=DARK, fg=ORANGE, pady=10)
password_label.grid(row=3, column=0)

# Entries

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "yourmail@yourmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
password_generate_button = Button(text="Generate Password", pady=4, command=generate_password)
password_generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, pady=5, command=add)
add_button.grid(row=5, column=1, columnspan=2)

search_button = Button(text="Search", pady=4, padx=39, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
