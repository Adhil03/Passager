from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_Entry.delete(0, END)
    password_Entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_Entry.get()
    password = password_Entry.get()
    username = username_Entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="OOPS!!!", message="Please Don't Leave Any Fields Empty!!!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details Entered :\n Email: {username}\n"
                                                              f"Password: {password}\n Is it Ok to Save ?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_Entry.delete(0, END)
                password_Entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager (Passager)")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_Label = Label(text="Website :", fg="black")
website_Label.grid(column=0, row=2)

username_Label = Label(text="Email/Username :")
username_Label.grid(column=0, row=3)
password_Label = Label(text="Password :")
password_Label.grid(column=0, row=4)

website_Entry = Entry(width=51)
website_Entry.grid(column=1, row=2, columnspan=2)
website_Label.focus()
username_Entry = Entry(width=51)
username_Entry.grid(column=1, row=3, columnspan=2)
username_Entry.insert(0, "adlpro@gmail.com")
password_Entry = Entry(width=32)
password_Entry.grid(column=1, row=4)
password_generate = Button(text="Generate Password", width=14, command=generate_password)
password_generate.grid(column=2, row=4)

Add_btn = Button(text="Add", width=43, command=save)
Add_btn.grid(column=1, row=5, columnspan=2)

window.mainloop()
