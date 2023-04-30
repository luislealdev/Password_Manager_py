from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_input.get()
    email = email_entry.get()
    password = password_entry.get()

    if (len(website) < 1 or len(email) < 1 or len(password) < 1):
        messagebox.showerror(title="Empty input",
                             message="Please don't leave any empty input")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"It is okay?\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(
                    f"{website} | {email} | {password}\n")

            website_input.delete(0, END)
            password_entry.delete(0, END)

            messagebox.showinfo(title={website}, message="Added correctly")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
my_pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_image)

canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_text = Label(text="Email/Username")
email_text.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.insert(0, "contacto@luisrrleal.com")
email_entry.grid(column=1, row=2,  columnspan=2)

password_text = Label(text="Password")
password_text.grid(column=0, row=3)
password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
