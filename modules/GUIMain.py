from tkinter import Tk
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from tkinter import Label


class GUIMain(object):
    def __init__(self, owner):
        self.owner = owner
        self.window = Tk()
        self.window.config(width=400, height=200, bg="black")
        self.button_login = Button(self.window, text="Log in", command=self.login)
        self.button_register = Button(self.window, text="register", command=self.register)
        self.button_logout = Button(self.window, text="Logout", command=self.logout)
        self.edit_username_var = StringVar()
        self.edit_username = Entry(self.window, text="", textvariable=self.edit_username_var)
        self.edit_password_var = StringVar()
        self.edit_password = Entry(self.window, text="", textvariable=self.edit_password_var, show="*")
        self.label_username = Label(self.window, text="Username")
        self.label_password = Label(self.window, text="Password")
        self.create_main_window()
        self.window.mainloop(0)

    def create_main_window(self):
        self.label_username.place(x=0, y=0, width=200, height=45)
        self.label_password.place(x=0, y=50, width=200, height=45)
        self.edit_username.place(x=200, y=0, width=200, height=45)
        self.edit_password.place(x=200, y=50, width=200, height=45)
        self.button_login.place(x=0, y=100, width=400, height=45)
        self.button_register.place(x=0, y=150, width=400, height=45)

    def login(self):
        print(self.owner.mediator.validate_username(self.edit_username_var.get()))
        print(self.owner.mediator.validate_password(self.edit_password_var.get()))
        response = self.owner.mediator.login(
            self.edit_username_var.get(),
            self.owner.mediator.hash_password(self.edit_password_var.get())
        )
        print(response)
        self.create_after_login()

    def create_after_login(self):
        self.label_password.place_forget()
        self.label_username.place_forget()
        self.edit_password.place_forget()
        self.edit_username.place_forget()
        self.button_register.place_forget()
        self.button_login.place_forget()
        self.button_logout.place(x=0, y=0, width=200, height=100)

    def register(self):
        print(self.owner.mediator.validate_username(self.edit_username_var.get()))
        print(self.owner.mediator.validate_password(self.edit_password_var.get()))
        response = self.owner.mediator.register_new_user(
            self.edit_username_var.get(),
            self.owner.mediator.hash_password(self.edit_password_var.get())
        )
        print(response)
        self.create_after_login()

    def logout(self):
        self.edit_username_var.set("")
        self.edit_password_var.set("")
        self.button_logout.place_forget()
        self.create_main_window()
        print("logout")
