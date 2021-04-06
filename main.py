from tkinter import messagebox
from tkinter import *

# CONSTANTS
DARK = "#383e56"
ORANGE = "#fb743e"


# PASS WORD GENERATOR


# SAVE PASSWORD

def add():
    website_name = website_input.get()
    email = email_input.get()
    password = password_input.get()
    with open("data.txt", "a") as data_file:
        data_file.write(f"Website Name: {website_name} | E-mail: {email} | Password: {password}\n")

    messagebox.showinfo(title="Password Added", message=f"Password for {website_name.upper()} added!")

    website_input.delete(0, "end")
    password_input.delete(0, "end")


# UI SETUP
window = Tk()
window.title("Password Manager")

# App Icon
img = Image("photo", file="images/logo.png")
window.call('wm', 'iconphoto', window._w, img)

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

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "yourmail@yourmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
password_generate_button = Button(text="Generate Password", pady=4)
password_generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, pady=5, command=add)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
