from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_input.grid(column=1, row=1, columnspan=2)

email_text = Label(text="Email/Username")
email_text.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2,  columnspan=2)

password_text = Label(text="Password")
password_text.grid(column=0, row=3)
password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()