import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


FONT_NAME = "San Francisco font"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  # for char in range(nr_letters):
  #   password_list.append(random.choice(letters))
  letter_list = [random.choice(letters) for char in range(nr_letters)]

  # for char in range(nr_symbols):
  #   password_list += random.choice(symbols)
  symbols_list = [random.choice(symbols) for char in range(nr_symbols)]

  # for char in range(nr_numbers):
  #   password_list += random.choice(numbers)
  numbers_list = [random.choice(numbers) for char in range(nr_numbers)]

  password_list = letter_list + symbols_list + numbers_list

  random.shuffle(password_list)

  # Joins everything inside a list/tuple in one word
  # password = ""
  # for char in password_list:
  #   password += char
  password = "".join(password_list)

# Insert the "generated password" onto the entry box
  password_entry.insert(0, password)

# Copy the "generated password" into the clipboard so that it's ready to be paste
  pyperclip.copy(password)

  #print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
  website_name = website_entry.get()
  username = username_entry.get()
  password = password_entry.get()
  new_data = {
    website_name: {
      "email": username,
      "password": password,
    }
              }

  if len(website_name) == 0 or len(password) == 0:
    messagebox.showinfo(title="Oops", message=f"Please make sure you haven't leave any fields empty.")
  else:
    try: # Try to open the file if it exist
      with open("data.json", "r") as f:
        # Reading old data
        data = json.load(f)
    except FileNotFoundError: # Creates a new file if file doesnt exist
      with open("data.json", "w") as f:
        json.dump(new_data, f, indent=4)
    else: # This line of code happens if try block on top occurs #
      # Updating old data with new data
      data.update(new_data)

      # Opens the file in write mode
      with open("data.json", "w") as f:
        # Saving/writes the updated data
        json.dump(data, f, indent=4)

    finally:
      print(data)
      website_entry.delete(0, END)
      password_entry.delete(0, END)

# open and read the file after the appending:
  f = open("data.txt", "r")
  print(f.read())

# ----------------- Find Password ----------------------------- #
def find_password():
  user_website_entry = website_entry.get().title()
  try:
    with open("data.json", "r") as f:
      data = json.load(f)
  except FileNotFoundError:
    messagebox.showinfo(title="Error", message="No Data File Found.")
  else:
    if user_website_entry in data:
        email = data[user_website_entry]["email"]
        password = data[user_website_entry]["password"]
        messagebox.showinfo(title=f"{user_website_entry}", message=f"Email: {email} \nPassword: {password}")
    else:
      messagebox.showinfo(title="Error", message=f"No details for {user_website_entry} exist.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



# Place the lock logo as a canvas on the window
lock_canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
# Create_image expects (x,y,image=PhotoImage())
lock_canvas.create_image(100, 100, image=lock_img)
# timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=1, row=1)
lock_canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 14))
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=(FONT_NAME, 14))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME, 14))
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=36)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "mm.alcaide38@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", font=(FONT_NAME, 13), command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, font=(FONT_NAME, 14), command=add_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, font=(FONT_NAME, 14), command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
