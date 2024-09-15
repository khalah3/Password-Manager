from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    #Using comprehension lists to generate a password.
    password_list1 = [random.choice(letters) for char in range(nr_letters)]

    password_list2 = [random.choice(symbols) for char in range(nr_symbols)]

    password_list3 = [random.choice(numbers) for char in range(nr_numbers)]

    password_final_list = password_list1+password_list2+password_list3

    random.shuffle(password_final_list)

    password = "".join(password_final_list)

    password_entry.insert(0, password)
    #copy password into clipboard using pyperclip
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website1 = website_entry.get()
    email1 = Email_username_entry.get()
    password1 = password_entry.get()

    #Warning for empty boxes
    if len(website1)==0 or len(password1)==0:
        messagebox.showinfo(title="oops", message="please don't leave empty boxes")
    # Messagebox to learn the concept about messageboxes from tkinter messagebox module
    else:

        is_ok = messagebox.askokcancel(title="website" , message=f"These are details entered:\n website={website1}\n email={email1}\n"
                                                      f"password={password1}\n Are these details ok?")
        # Append the data.txt file with the information provided from the tkinter window
        if is_ok:

            with open("data.txt", "a") as data_file:
                data_file.write(f"{website1} , {email1} , {password1}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Setting up window,canvas, labels, entries, and buttons.
window = Tk()
window.title("Password Manager")
window.config(bg="white")
window.config(padx=50, pady=50)

canvas = Canvas(width=150, height=150, bg='white')
logo_img = PhotoImage(file="logo.png")
canvas.create_image(75, 75, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg='white')
website_label.grid(row=1, column=0)

Email_Username_label = Label(text="Email/Username:", bg='white')
Email_Username_label.grid(row=2, column=0)

Password_label = Label(text="Password:", bg='white')
Password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1)

Email_username_entry = Entry(width=35)
Email_username_entry.grid(row=2, column=1, columnspan=2)
Email_username_entry.insert(0, "ahmad.khalifeh@gmail.com")

# triggering a function with the command "generate password" button
password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(row=3, column=2)

# Adding data to data.txt using the Add button
Add_button = Button(text="Add_to_data.txt", width=37, command=save)
Add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
