from tkinter import *
import sys
from datetime import time
import sql_funcs

'''
File contains:
    - functions for handling UI events
    - UI object initialization
    - UI object placement
    - handling user input
    - references and calls to 'sql_funcs.py' to handle sql code
'''

''' FUNCTIONS FOR HANDLING UI EVENTS '''
# handle events allow for sample text to show up in input fields
def handle_un_focus_in(_):
    if user_name_entry.get() == "username":
        user_name_entry.delete(0, END)
        user_name_entry.config(fg='black')

def handle_un_focus_out(_):
    if user_name_entry.get() == "":
        user_name_entry.delete(0, END)
        user_name_entry.config(fg='gray')
        user_name_entry.insert(0, "username")

def handle_upw_focus_in(_):
    if user_pw_entry.get() == "password":
        user_pw_entry.delete(0, END)
        user_pw_entry.config(fg='black')

def handle_upw_focus_out(_):
    if user_pw_entry.get() == "":
        user_pw_entry.config(fg='gray')
        user_pw_entry.insert(0, "password")

def handle_an_focus_in(_):
    if admin_name_entry.get() == "username":
        admin_name_entry.delete(0, END)
        admin_name_entry.config(fg='black')

def handle_an_focus_out(_):
    if admin_name_entry.get() == "":
        admin_name_entry.config(fg='gray')
        admin_name_entry.insert(0, "username")

def handle_apw_focus_in(_):
    if admin_pw_entry.get() == "password":
        admin_pw_entry.delete(0, END)
        admin_pw_entry.config(fg='black')

def handle_apw_focus_out(_):
    if admin_pw_entry.get() == "":
        admin_pw_entry.config(fg='gray')
        admin_pw_entry.insert(0, "password")

def open_user_window():
    user_window = Toplevel(root)
    icon = PhotoImage(file="tree.png")
    user_window.iconphoto(False, icon)
    user_window.title('Search the Kickass Cities Database')
    user_header_col = Frame(user_window)
    user_header_col.grid(row=0, column=0, columnspan=2)
    user_header_label = Label(user_header_col, text="Find more about your city", font=('TkDefaultFont', 16, 'bold'))
    user_header_label.grid(row=0, column=0)

def open_admin_window():
    admin_window = Toplevel(root)
    icon = PhotoImage(file="tree.png")
    admin_window.iconphoto(False, icon)
    admin_window.title('Update the Kickass Cities Database')
    admin_header_col = Frame(admin_window)
    admin_header_col.grid(row=0, column=0, columnspan=2)
    admin_header_label = Label(admin_header_col, text="Update data for cities", font=('TkDefaultFont', 16, 'bold'))
    admin_header_label.grid(row=0, column=0)

def user_login_submit():
    username = user_name_entry.get()
    password = user_pw_entry.get()
    # 'authenticate' password
    if username == 'username' and password == 'password':
        open_user_window()

def admin_login_submit():
    username = admin_name_entry.get()
    password = admin_pw_entry.get()
    # 'authenticate' password
    if username == 'username' and password == 'password':
        open_admin_window()

# begin UI event loop
root = Tk()

# change program icon
icon = PhotoImage(file="tree.png")
root.iconphoto(False, icon)
root.title('Kickass cities Database')

# establish frames for each section of window
login_header_col = Frame(root)
user_col = Frame(root)
admin_col = Frame(root)

''' LOGIN SCREEN '''

# put the frames on the window using a 'grid'
login_header_col.grid(row=0, column=0, columnspan=2)
user_col.grid(row=1, column=0, sticky='nsew', padx=(10,4), pady=(4,10))
admin_col.grid(row=1, column=1, sticky='nsew', padx=(4,10), pady=(4,10))

# create and place label objects for login screen
header_label = Label(login_header_col, text="Cities Database Login", font=('TkDefaultFont', 16, 'bold'))
header_label.grid(row=0, column=0)
user_login_label = Label(user_col, text="User Login:", font=('TkDefaultFont', 12, 'bold'))
user_login_label.grid(row=0, column=0)
admin_login_label = Label(admin_col, text="Admin Login:", font=('TkDefaultFont', 12, 'bold'))
admin_login_label.grid(row=0, column=0)

# create and place text field objects for login screen
user_name_entry = Entry(user_col, width=30, bg='white', fg='gray')
user_name_entry.grid(row=1, column=0, padx=8, pady=4)
user_name_entry.insert(0, "username")
user_name_entry.bind("<FocusIn>", handle_un_focus_in)
user_name_entry.bind("<FocusOut>", handle_un_focus_out)

user_pw_entry = Entry(user_col, width=30, bg='white', fg='gray')
user_pw_entry.grid(row=2, column=0, columnspan=1, padx=8, pady=4)
user_pw_entry.insert(0, "password")
user_pw_entry.bind("<FocusIn>", handle_upw_focus_in)
user_pw_entry.bind("<FocusOut>", handle_upw_focus_out)

admin_name_entry = Entry(admin_col, width=30, bg='white', fg='gray')
admin_name_entry.grid(row=1, column=0, padx=8, pady=4)
admin_name_entry.insert(0, "username")
admin_name_entry.bind("<FocusIn>", handle_an_focus_in)
admin_name_entry.bind("<FocusOut>", handle_an_focus_out)

admin_pw_entry = Entry(admin_col, width=30, bg='white', fg='gray')
admin_pw_entry.grid(row=2, column=0, columnspan=1, padx=8, pady=4)
admin_pw_entry.insert(0, "password")
admin_pw_entry.bind("<FocusIn>", handle_apw_focus_in)
admin_pw_entry.bind("<FocusOut>", handle_apw_focus_out)

# create and place submit button for login
user_login_submit_button = Button(user_col, text="Submit", padx=8, pady=6, width=10, command=user_login_submit)
user_login_submit_button.grid(row=3, column=0, pady=(16,4))

admin_login_submit_button = Button(admin_col, text="Submit", padx=8, pady=6, width=10, command=admin_login_submit)
admin_login_submit_button.grid(row=3, column=0, pady=(16,4))


# conclude UI event loop
root.mainloop()