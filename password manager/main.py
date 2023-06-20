from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
import _json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ["a", "b", "q","W","e","r","t","y","u","i","o","p","d","f","g","h","j","k","l",
           "z","x","c","v","b","n","m",'A', 'B', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 
           'O', 'P', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

numbers = [0,1,2,3,4,5,6,7,8,9]

symbols = ["!",'#','$','%','^',"&", "*","(",")","_","+","=","?","/"]
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbol = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_numbers)]

    password_numbers = [str(random.choice(numbers)) for _ in range(nr_numbers)]

    password_list = password_numbers+password_letter+password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, f"{password}")

    pyperclip.copy(password)
# for ch in password_list:
#     password+=ch

# ---------------------------- SAVE PASSWORD ------------------------------- #

def find():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File found")        
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email:{email}\npassowrd:{password}")
        else:
            messagebox.showinfo(title="Error", message="No data File found")        
                     
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    new_data = {
        website:{
            "email":email,
            "password":password
        },
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="information not filled", message="complete the information") 

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:    
                with open("data.json", "r") as data_file: 
                    data = json.load(data_file)
                               
            except FileNotFoundError:
                with open("data.json", "w")as data_e:
                    json.dump(new_data, data_e)
            
            else:
                data.update(new_data)
                with open("data.json", "w") as data_fi:
                    json.dump(data, data_fi, indent=4)
            finally:                    
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=43,pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)
#labels
website_lab = Label(text="Website")
website_lab.grid(row=1, column=0)

email_lab=Label(text="Eamil")
email_lab.grid(row=2, column=0)

password_lab =Label(text="Password")
password_lab.grid(row=3, column=0)

#Entryes
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2)
email_entry.insert(0, "omaratef@gmail.com")

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()
#button
seearch_button = Button(text="Search", width=15, command=find)
seearch_button.grid(column=2, row=1)
generated_passsword_butt = Button(text="Generate Password", command=generate_password)
generated_passsword_butt.grid(row=3, column=2)
add_button = Button(text = "Add", width=30, command=save)
add_button.grid(row=4, column=1)










window.mainloop()