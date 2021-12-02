import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import datetime
from PIL import ImageTk, Image
import mysql.connector as data
from dateutil.relativedelta import relativedelta
import time

class Registration:
    def __init__(self, root):
        self.root = root
        self.root.resizable(width=0, height=0)
        self.setup_interface()
        self.make_Frame()
        self.write_title()
        self.create_widget()
        self.register_button()

    def setup_interface(self):
        self.root.title("Registration Form")
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight() - 60

        self.root.geometry("%dx%d+0+0" % (width, height))
        self.root.config(bg="sky blue")

    def make_Frame(self):
        self.Reg_Frame = tk.LabelFrame(self.root, pady=90, bg="#d4d1ce")
        self.Reg_Frame.place(x=500, y=50, width=600, height=700)

    def write_title(self):
        self.title = tk.Label(self.root, text="REGISTRATION FORM", font=("oblique", 18), bg="#d4d1ce")
        self.title.place(x=640, y=90)

    def create_widget(self):
        # Label for First Name
        self.first_name = tk.Label(self.Reg_Frame, text="First Name", bg="#d4d1ce")
        self.first_name.grid(row=0, column=0, sticky='W', padx=(38, 0))
        # Entry widget for First Name
        self.first_name_entry = tk.Entry(self.Reg_Frame, borderwidth=4, width=30)
        self.first_name_entry.grid(row=1, column=0, padx=(40, 0), ipady=4)

        # Label for Last Name
        self.last_name = tk.Label(self.Reg_Frame, text="Last Name", bg="#d4d1ce")
        self.last_name.grid(row=0, column=1, sticky='W', padx=(116, 0))
        # Entry widget for Last Name
        self.last_name_entry = tk.Entry(self.Reg_Frame, borderwidth=4, width=30)
        self.last_name_entry.grid(row=1, column=1, padx=(120, 50), ipady=4)

        # Label for Mobile Number
        self.mobile_number = tk.Label(self.Reg_Frame, text="Mobile Number", bg="#d4d1ce")
        self.mobile_number.grid(row=2, column=0, sticky='W', padx=(38, 0), pady=(40, 0))
        # Entry widget for Mobile Number
        self.mobile_number_entry = tk.Entry(self.Reg_Frame, borderwidth=4, width=30)
        self.mobile_number_entry.grid(row=3, column=0, padx=(40, 0), ipady=4)

        # Label for Gmail
        self.gmail_name = tk.Label(self.Reg_Frame, text="Gmail Name", bg="#d4d1ce")
        self.gmail_name.grid(row=2, column=1, sticky='W', padx=(116, 0), pady=(40, 0))
        # Entry widget for Gmail
        self.gmail_name_entry = tk.Entry(self.Reg_Frame, borderwidth=4, width=30)
        self.gmail_name_entry.grid(row=3, column=1, padx=(120, 50), ipady=4)

        # Label for User Name
        self.user_name = tk.Label(self.Reg_Frame, text="User Name", bg="#d4d1ce")
        self.user_name.grid(row=4, column=0, pady=(40, 0), sticky='W', padx=(38, 0))
        # Entry widget for User Name
        self.user_name_entry = tk.Entry(self.Reg_Frame, borderwidth=4, width=30)
        self.user_name_entry.grid(row=5, column=0, padx=(40, 0), ipady=4)

        # Label for D.O.B
        self.date_of_birth = tk.Label(self.Reg_Frame, text="D.O.B(MM/DD/YYYY) ", bg="#d4d1ce")
        self.date_of_birth.grid(row=4, column=1, sticky='W', padx=(116, 0), pady=(40, 0))
        # DateEntry widget for D.O.B
        # self.date_of_birth_cal = DateEntry(self.Reg_Frame, borderwidth=4, width=28, justify='center')
        self.date_of_birth_cal = tk.Entry(self.Reg_Frame, borderwidth=4, width=28)
        self.date_of_birth_cal.grid(row=5, column=1, padx=(120, 50), ipady=4)

        # Label for Password
        self.password = tk.Label(self.Reg_Frame, text="Password", bg="#d4d1ce")
        self.password.grid(row=6, column=0, pady=(40, 0), sticky='W', padx=(38, 0))
        # Entry widget for Password
        bullet = "\u2022"
        self.password_entry = tk.Entry(self.Reg_Frame, show=bullet, borderwidth=4, width=30)
        self.password_entry.grid(row=7, column=0, padx=(40, 0), ipady=4)

        # Label for Confirm Password
        self.confirm_password = tk.Label(self.Reg_Frame, text="Confirm Password", bg="#d4d1ce")
        self.confirm_password.grid(row=6, column=1, pady=(40, 0), sticky='W', padx=(116, 0))
        # Entry widget for Confirm Password
        self.confirm_password_entry = tk.Entry(self.Reg_Frame, show=bullet, borderwidth=4, width=30)
        self.confirm_password_entry.grid(row=7, column=1, padx=(120, 50), ipady=4)

        self.box_value = tk.StringVar()
        # Label for Security Question
        self.security_que = tk.Label(self.Reg_Frame, text="Security Question", bg="#d4d1ce")
        self.security_que.grid(row=8, column=0, pady=(40, 0), sticky='W', padx=(38, 0))
        # Combobox for Security Question
        self.security_que_cmd = ttk.Combobox(self.Reg_Frame, textvariable=self.box_value, state='readonly',justify='center', width=27)
        self.security_que_cmd['values'] = ["Select", 'Your favourie game', 'Your dream job', 'Name of first school','Your Pet name']
        self.security_que_cmd.grid(row=9, column=0, padx=(40, 0), ipady=4)
        self.security_que_cmd.current(0)

        # Label for Answer
        self.security_ans = tk.Label(self.Reg_Frame, text="Answer", bg="#d4d1ce")
        self.security_ans.grid(row=8, column=1, pady=(40, 0), sticky='W', padx=(116, 0))
        # #Entry widget for Answer
        self.security_ans_entry = tk.Entry(self.Reg_Frame, borderwidth=4, width=30)
        self.security_ans_entry.grid(row=9, column=1, padx=(120, 50), ipady=4)

        # Button for Term & Condition
        self.condtion_value = tk.IntVar()
        self.condtion = tk.Checkbutton(self.Reg_Frame, variable=self.condtion_value,text="I agree the Term & Condition", bg="#d4d1ce")
        self.condtion.grid(row=10, column=0, pady=(40, 0), padx=(20, 0))

        # Image for Back
        self.back_image = ImageTk.PhotoImage(file="back_button.jpg")
        self.back_image_button = tk.Button(self.root, image=self.back_image, command=self.go_back)
        self.back_image_button.place(x=510, y=65)

    def make_empty(self):
        self.first_name_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')
        self.user_name_entry.delete(0, 'end')
        self.mobile_number_entry.delete(0, 'end')
        self.gmail_name_entry.delete(0, 'end')
        self.date_of_birth_cal.delete(0, 'end')
        self.security_que_cmd.current(0)
        self.security_ans_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.confirm_password_entry.delete(0, 'end')
        self.condtion.deselect()

    def go_back(self):
        self.Reg_Frame.destroy()
        self.title.destroy()
        self.register_butt.destroy()
        self.back_image_button.destroy()
        lgn = Login(root)

    def check_error(self):
        if self.first_name_entry.get() == "":
            messagebox.showerror("Error", "User have not enter the first Name")
            return False
        elif self.last_name_entry.get() == "":
            messagebox.showerror("Error", "User have not enter the Last Name")
            return False
        elif self.mobile_number_entry.get() == "":
            messagebox.showerror("Error", "User have not enter Phone number")
            return False
        elif self.gmail_name_entry.get() == "":
            messagebox.showerror("Error", "User have not enter gmail")
            return False
        elif self.user_name_entry.get() == "":
            messagebox.showerror("Error", "User have not enter the username")
            return False
        elif self.password_entry.get() == "":
            messagebox.showerror("Error", "User have not enter the password")
            return False
        elif self.confirm_password_entry.get() == "":
            messagebox.showerror("Error", "User have not confirm the password")
            return False
        elif self.security_ans_entry.get() == "":
            messagebox.showerror("Error", "User have not fill the security answer")
            return False
        elif self.box_value.get() == "Select":
            messagebox.showerror("Error", "User have not selected the security question")
            return False
        elif self.condtion_value.get() == 0:
            messagebox.showerror("Error", "User have not accepted term and conditon")
            return False
        elif not self.password_entry.get() == self.confirm_password_entry.get():
            messagebox.showerror("Error", "Confirm password is not matching with set password")
            self.confirm_password_entry.delete(0, 'end')
            return False
        elif len(self.password_entry.get()) < 6:
            messagebox.askretrycancel("Error","Password must be greater than 6 digit and Contain '0-9,'special character','Captial letter'")
            return False

        try:
            dob = self.date_of_birth_cal.get().split('/')
            dob = list(map(int, dob))
            self.d2 = datetime.date.today()
            d1 = datetime.date(int("20" + str(dob[2]) if len(str(dob[2])) == 2 else dob[2]), dob[0], dob[1])
            print(d1, " a ", self.d2)
            self.dob = str(d1)
            print(d1, type(self.dob))
            print(self.d2, type(self.d2))
            self.created = str(self.d2)
            self.phone_number = int(self.mobile_number_entry.get())
            if d1 > self.d2:
                messagebox.showerror("Error", "User have enter wrong date of birth")
                return False
            if relativedelta(self.d2, d1).years < 15:
                messagebox.showerror("Error", "User age must be greater than 15 years ")
                return False
            else:
                self.age = relativedelta(self.d2, d1).years
        except Exception as exec:
            messagebox.showerror("Error", str(exec))
            return False

        try:
            conn = data.connect(host="localhost", user="root", password="12345",database="practice")
            with conn.cursor() as cursor:
                cursor.execute(f"select count(*) from user_detail where user_name ='{self.user_name_entry.get()}'")
                result1 = cursor.fetchone()[0]
                if result1:
                    messagebox.showerror("Error", "user_name is already taken")
                    return False
                print("hello")
                cursor.execute(f"select count(*) from user_detail where gmail ='{self.gmail_name_entry.get()}'")
                result2 = cursor.fetchone()[0]
                if result2:
                    messagebox.showerror("Error", "gmail is already used")
                    return False

                conn.commit()
                conn.close()

            return True
        except Exception as ex:
            print(ex)
            return False

    def register(self):
        check_user_name = "Select "

        print("|move to register|")
        if not self.check_error():
            return
        try:
            conn = data.connect(host="localhost", user="root", password="12345",database="practice")
            with conn.cursor() as cursor:
                cursor.execute(
                    f"insert into user_detail values('{self.user_name_entry.get()}','{self.first_name_entry.get()}','{self.last_name_entry.get()}',{self.phone_number},'{self.gmail_name_entry.get()}','{self.dob}',{self.age},'{self.password_entry.get()}','{self.box_value.get()}','{self.security_ans_entry.get()}','{self.created}')")
                conn.commit()

        except Exception as ex:
            print(ex)
            return

        messagebox.showinfo("Success", "Your registration has been successful")
        self.make_empty()

    def register_button(self):
        self.register_butt = tk.Button(self.root, text="Register", bg="#11d535", bd=4, command=self.register)
        self.register_butt.place(x=750, y=650, width=120, height=50)


class Login:
    def __init__(self, root):
        self.root = root
        self.setup_interface()
        self.count_intiliaze()
        self.admin_login()
        self.create_widget()

    def setup_interface(self):
        self.root.title("Login Form")

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight() - 60
        self.root.geometry("%dx%d+0+0" % (width, height))

        self.root.resizable(width=0, height=0)
        self.root.config(bg="sky blue")

    def move_to_user_dashboard(self):
        self.Login_Frame.destroy()
        self.admin_login_button.destroy()
        self.user_login_button.destroy()
        a = Dashboard(self.root)

    def check_login_detail(self):
        if not self.box_value.get() == 'Temproary User':
            messagebox.showerror("Error", "Yet now no student or teacher create by admin")

        try:
            conn = data.connect(host="localhost", user="root", password="12345",database="practice")
            with conn.cursor() as cursor:
                cursor.execute(f"select count(*) from user_detail where user_name ='{self.user_name_entry.get()}'")
                result1 = cursor.fetchone()[0]
                if not result1:
                    messagebox.showerror("Error", "user_name is not wrong")
                    return False

                cursor.execute(f"select password from user_detail where user_name ='{self.user_name_entry.get()}'")
                result2 = cursor.fetchone()[0]
                if result2 == self.password_entry.get():
                    return True
                else:
                    messagebox.showerror("Error", "Password is not wrong")

                conn.commit()
                conn.close()

            return False
        except Exception as ex:
            print(ex)
            return False

    def login_user(self):
        if self.user_name_entry.get() == "":
            messagebox.showerror("Error", "You have not enter username")
            return
        if self.password_entry.get() == "":
            messagebox.showerror("Error", "you have not enter password")
            return
        if self.box_value.get() == 'Select':
            messagebox.showerror("Error", "You have not choose 'what you are'")
            return
        if self.check_login_detail():
            self.move_to_user_dashboard()

    def user_login(self):
        self.user_login_button['state'] = 'disable'
        self.admin_login_button['state'] = 'active'
        self.user_login_button.config(bg='#98ff98', font=('Helvetica 15 underline'))
        self.admin_login_button.config(bg="#d8e4bc", font=("Optima", 15))
        self.Login_Frame.destroy()
        # self.back_image_button.destroy()

        self.Login_Frame = tk.LabelFrame(self.root, pady=90, bg="#eadbc8")
        self.Login_Frame.place(x=550, y=142, width=450, height=600)

        self.title = tk.Label(self.Login_Frame, text="User Login", font=("Optima", 24, "bold"), bg="#eadbc8")
        self.title.place(x=120, y=-35)

        self.user_name_label = tk.Label(self.Login_Frame, text="UserName/Registration No.", font=("Optima", 22), bg="#eadbc8")
        self.user_name_label.grid(row=0, column=0, padx=(60, 0), pady=(85, 0), sticky='W')
        self.user_name_entry = tk.Entry(self.Login_Frame, width=50)
        self.user_name_entry.grid(row=1, column=0, ipady=10, padx=(60, 0))
        bullet = '\u2022'
        self.password_label = tk.Label(self.Login_Frame, text="Password", font=("Optima", 22), bg="#eadbc8")
        self.password_label.grid(row=2, column=0, padx=(60, 0), pady=(25, 0), sticky='W')
        self.password_entry = tk.Entry(self.Login_Frame, show=bullet, width=50)
        self.password_entry.grid(row=3, column=0, ipady=10, padx=(60, 0))

        self.box_value = tk.StringVar()
        self.chose_label = tk.Label(self.Login_Frame, text="You are", bg="#eadbc8", font=("Optima", 22))
        self.chose_label.grid(row=4, column=0, padx=(60, 0), pady=(25, 0), sticky='W')
        self.choose_combobox = ttk.Combobox(self.Login_Frame, textvariable=self.box_value, state='readonly',justify='center', width=45)
        self.choose_combobox['value'] = ['Select', 'Student', 'Faculty', 'Temproary User']
        self.choose_combobox.grid(row=5, column=0, ipady=10, padx=(60, 0))
        self.choose_combobox.current(0)

        self.login_butt = tk.Button(self.Login_Frame, text="Login", bg="#d0f0c0", command=self.login_user)
        self.login_butt.place(x=145, y=395, width=120, height=50)

        self.new_frame = tk.Frame(self.Login_Frame, bg="#eadbc8")
        self.new_frame.place(x=140, y=465)

        self.ask_register = tk.Label(self.new_frame, text="Don't have an account?  ", bg="#eadbc8")
        self.ask_register.grid(row=0, column=0)

        self.ask_register2 = tk.Button(self.new_frame, text="Register", fg="blue", bg="#eadbc8",command=self.go_to_register)
        self.ask_register2.grid(row=0, column=1)

    def admin_login(self):
        if self.count > 0:
            self.Login_Frame.destroy()
            self.admin_login_button['state'] = 'disable'
            self.user_login_button['state'] = 'active'
            self.admin_login_button.config(bg='#98ff98', font=('Helvetica 15 underline'))
            self.user_login_button.config(bg="#d8e4bc", font=("Optima", 15))

        self.count += 1

        self.Login_Frame = tk.LabelFrame(self.root, pady=90, bg="#eadbc8")
        self.Login_Frame.place(x=550, y=142, width=450, height=600)
        self.title = tk.Label(self.Login_Frame, text="Admin Login", font=("Optima", 24, "bold"), bg="#eadbc8")
        self.title.place(x=120, y=-35)
        self.user_name_label = tk.Label(self.Login_Frame, text="Username/gmail", font=("Optima", 22), bg="#eadbc8")
        self.user_name_label.grid(row=0, column=0, padx=(60, 0), pady=(85, 0), sticky='W')
        self.user_name_entry = tk.Entry(self.Login_Frame, width=27, font=("oblique", 15))
        self.user_name_entry.grid(row=1, column=0, ipady=4, padx=(60, 0))
        bullet = '\u2022'
        self.password_label = tk.Label(self.Login_Frame, text="Password", font=("Optima", 22), bg="#eadbc8")
        self.password_label.grid(row=2, column=0, padx=(60, 0), pady=(40, 0), sticky='W')
        self.password_entry = tk.Entry(self.Login_Frame, show=bullet, width=50)
        self.password_entry.grid(row=3, column=0, ipady=10, padx=(60, 0))

        self.login_butt = tk.Button(self.Login_Frame, text="Login", bg="#d0f0c0", command=self.login_admin)
        self.login_butt.place(x=145, y=350, width=120, height=50)

        self.new_frame = tk.Frame(self.Login_Frame, bg="#eadbc8")
        self.new_frame.place(x=140, y=420)

        self.ask_register = tk.Label(self.new_frame, text="Don't have an account?  ", bg="#eadbc8")
        self.ask_register.grid(row=0, column=0)

        self.ask_register2 = tk.Button(self.new_frame, text="Register", fg="blue", bg="#eadbc8",command=self.go_to_register)
        self.ask_register2.grid(row=0, column=1)

    def go_to_register(self):
        self.Login_Frame.destroy()
        self.admin_login_button.destroy()
        self.user_login_button.destroy()
        reg = Registration(self.root)

    def count_intiliaze(self):
        self.count = 0

    def create_widget(self):
        self.admin_login_button = tk.Button(self.root, text="Admin", font=("Optima", 14), bg="#eadbc8",justify='center', bd=4, command=self.admin_login)
        self.admin_login_button.place(x=550, y=100, width=225)
        self.admin_login_button['state'] = 'disable'
        self.admin_login_button.config(bg='#98ff98', font=('Helvetica 15 underline'))

        self.user_login_button = tk.Button(self.root, text="Faculty/Student", bg="#d8e4bc", justify='center', bd=4,font=("Optima", 15), command=self.user_login)
        self.user_login_button.place(x=775, y=100, width=225)

    def login_admin(self):

        if not self.user_name_entry.get() == "nitin_saini_08":
            messagebox.showerror("Error", "You have not enter username or username is not exit")
            return
        if not self.password_entry.get() == "12345":
            messagebox.showerror("Error", "you have not enter password or password is wrong")
            return


        self.move_to_user_dashboard()


class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="#C0C0C0")

        self.make_frame()
        self.root.title("UMS")
        self.left_side_panel()
        self.right_panel_upper()
        self.right_panel_first()
        self.insertdata()
        self.filling_data()
        self.digital_time()
        self.right_panel_second()
        self.right_side_panel_third()

    def make_frame(self):
        self.width_screen = self.root.winfo_screenwidth()
        self.height_screen = self.root.winfo_screenheight()
        self.ums_heading = tk.Frame(self.root, bd=2, bg="green")
        self.ums_heading.place(x=0, y=0, width=self.width_screen, height=50)
        self.title = tk.Label(self.ums_heading, text="University Management System", font=('Aria', 25, 'bold'),bg="green")
        self.title.pack()

    def change_user_pass(self):
        self.new_window = tk.Tk()
        self.new_window.geometry('1000x700+200+10')
        self.new_window.config(bg='#453541')

        self.main_change_password_frame = tk.Frame(self.new_window)
        self.main_change_password_frame.place(relx=0.2,rely=0.2,width=600,height=400)

        self.heading_frame_change_password = tk.Frame(self.main_change_password_frame)
        self.heading_frame_change_password.pack()

        self.change_password_heading = tk.Label(self.heading_frame_change_password, text= "Change Password", font=("Oblique",25))
        self.change_password_heading.pack()


        self.password_change_frame = tk.Frame(self.main_change_password_frame)
        self.password_change_frame.place(relx=0,rely=0)

        self.user_name_label_change_password = tk.Label(self.password_change_frame, text="Enter Your username")
        self.user_name_label_change_password.grid(row = 0 , column =0,padx=10,pady=10)

        self.user_name_entry_change_password = tk.Entry(self.password_change_frame)
        self.user_name_entry_change_password.grid(row=0, column=1,padx=10,pady=10)

        self.old_password_label = tk.Label(self.password_change_frame, text = "Enter Your Old Password : ")
        self.old_password_label.grid(row = 0 , column =2,padx=10,pady=10)

        self.old_password_entry = tk.Entry(self.password_change_frame)
        self.old_password_entry.grid(row=0, column=3,padx=10,pady=10)

        self.new_password_label = tk.Label(self.password_change_frame, text="Enter Your new Password : ")
        self.new_password_label.grid(row =1 , column = 0,padx=10,pady=10)

        self.new_password_entry = tk.Entry(self.password_change_frame)
        self.new_password_entry.grid(row=1, column=1,padx=10,pady=10)

        self.confirm_new_password_label = tk.Label(self.password_change_frame, text="Confirm Your new Password : ")
        self.confirm_new_password_label.grid(row=1, column=2, padx=10, pady=10)

        self.confirm_new_password_entry = tk.Entry(self.password_change_frame)
        self.confirm_new_password_entry.grid(row=1, column=3, padx=10, pady=10)

        self.submit_password_change_button = tk.Button(self.password_change_frame,text="Change Password")
        self.submit_password_change_button.grid(row=2,column=0,columnspan=4)

        self.new_window.mainloop()


    def left_side_panel(self):
        self.left_frame = tk.Frame(self.root, bg='pink')
        self.left_frame.place(x=0, y=50, width=150, height=self.height_screen)

        self.dashboard_button = tk.Button(self.left_frame, text="Dashboard", font=("oblique", 14), bd=4, width=155,height=6)
        self.dashboard_button.pack()
        self.dashboard_button['state'] = 'disable'

        self.student_management_system = tk.Button(self.left_frame, text="Student\n Management \nSystem",font=("oblique", 14), bd=4, width=155, height=6)
        self.student_management_system.pack()

        self.faculty_management_system = tk.Button(self.left_frame, text="Faculty \n Management \nSystem",font=("oblique", 14), bd=4, width=155, height=6)
        self.faculty_management_system.pack()

        self.change_password = tk.Button(self.left_frame, text="Change \nPassword", font=("oblique", 14), bd=4,width=155, height=6 , command = self.change_user_pass)
        self.change_password.pack()

        self.about_me = tk.Button(self.left_frame, text="About Me", font=("oblique", 14), bd=4, width=155, height=5)
        self.about_me.pack()

    def right_panel_upper(self):
        print("hello")
        self.blue_box = tk.Frame(self.root)
        self.blue_box.place(x=225, y=100, width=350, height=125)
        self.blue_box.config(bg='#0000d6')
        self.total_user = tk.Label(self.blue_box, text="Total User", font=("Oblique", 20), padx=15, pady=40,bg="#0000d6", fg="white")
        self.total_user.pack(side="left")

        self.red_box = tk.Frame(self.root)
        self.red_box.place(x=650, y=100, width=350, height=125)
        self.red_box.config(bg='#ff1f1f')
        self.total_user = tk.Label(self.red_box, text="Total Student", font=("Oblique", 20), padx=15, pady=40,bg="#ff1f1f", fg="white")
        self.total_user.pack(side="left")

        self.purple_box = tk.Frame(self.root)
        self.purple_box.place(x=1075, y=100, width=350, height=125)
        self.purple_box.config(bg='#8800f0')
        self.total_user = tk.Label(self.purple_box, text="Total Faculty", font=("Oblique", 20), padx=15, pady=40,bg="#8800f0", fg="white")
        self.total_user.pack(side="left")

    def right_panel_first(self):
        self.recent_user = tk.Frame(self.root)
        self.recent_user.place(x=225, y=300, width=520, height=300)
        self.recent_user.config(bg="white")

        self.recent_user_add_heading = tk.Frame(self.recent_user, bg="#a60ddc")
        self.recent_user_add_heading.place(height=40, width=520)

        self.label_user_added = tk.Label(self.recent_user_add_heading, text="Recent Added User List",font=("oblique", 16), bg="#a60ddc", fg="white")
        self.label_user_added.grid(row=0, column=0, pady=(4, 0))

        self.recent_data = tk.Frame(self.recent_user)
        self.recent_data.place(y=40, height=254, width=520)



    def insertdata(self):
        columns = ('username', 'firstname', 'gmail', 'created')

        style = ttk.Style()
        style.theme_use("clam")
        # style.configure('Treeview.Heading', font=('oblique', 12,'bold'), background="black", foreground="red")
        style.configure("Treeview.Heading", background="#4a4a4a", foreground="white", font=('oblique', 12, 'bold'))

        style.configure("Treeview",foreground="black",rowheight=30)
        style.map('Treeview', background=[('selected', 'black')])

        tree = ttk.Treeview(self.recent_data, columns=columns, show='headings', selectmode='browse')
        tree.column("username", anchor='center', stretch='NO', width=130)
        tree.heading('username', text='User Name')
        tree.column("firstname", anchor='center', stretch='NO', width=130)
        tree.heading('firstname', text='Name')
        tree.column("gmail", anchor='center', stretch='NO', width=130)
        tree.heading('gmail', text='Gmail')
        tree.column("created", anchor='center', stretch='NO', width=130)
        tree.heading('created', text='Created')

        tree.grid(row=0, column=0)

        # connect and retreive the data from database
        con1 = data.connect(host="localhost", user="root", password="12345",database="practice")
        cur1 = con1.cursor()
        cur1.execute("SELECT * FROM user_detail")
        rows = cur1.fetchall()
        self.total_user_count = len(rows)
        for num, row in enumerate(rows):
            if num < 7:
                print(row)
                tree.insert("", tk.END, values=(row[0], row[1] + " " + row[2], row[4], row[10]))
        con1.close()



    def filling_data(self):
        self.total_user_count_label = tk.Label(self.blue_box, text=self.total_user_count, padx=30, font=("oblique", 35),bg="#0000d6", fg="white")
        self.total_user_count_label.pack(side="right")

        self.total_student_count = 3
        self.total_student_count_label = tk.Label(self.red_box, text=self.total_student_count, padx=30,font=("oblique", 35), bg="#ff1f1f", fg="white")
        self.total_student_count_label.pack(side="right")

        self.total_faculty_count = 0
        self.total_faculty_count_label = tk.Label(self.purple_box, text=self.total_faculty_count, padx=30,font=("oblique", 35), bg="#8800f0", fg="white")
        self.total_faculty_count_label.pack(side="right")


    def digital_time(self):
        self.clock_frame = tk.Frame(self.root,bg="black")
        self.clock_frame.place(x=805,y=660,width = 640,height=100)

        def show_time():
            current_time = time.strftime(' Time is :- %H:%M:%S %p    Day :- %a')
            display.config(text=current_time)
            display.after(100, show_time)

        display = tk.Label(self.clock_frame, font=('Helvetica', 28),bg="gray8", fg="yellow",width = 640,height=100)
        display.pack(anchor='e')
        show_time()



    def search_user(self):
        # con2 = data.connect(host="localhost", user="root", password="12345", database="practice")
        # cur2 = con2.cursor()
        #
        # cur1.execute("select * from user_detail where ")
        pass


    def right_panel_second(self):
        self.enter_detail_for_search_frame = tk.Frame(self.root)
        self.enter_detail_for_search_frame.place(x=800, y=300, width=650, height=300)
        self.recent_user.config(bg="white")

        self.search_user_heading = tk.Frame(self.enter_detail_for_search_frame, bg="#a60ddc")
        self.search_user_heading.place(height=40, width=650)

        self.search_user_detail = tk.Frame(self.enter_detail_for_search_frame, bg="blue")
        self.search_user_detail.place(y=40,height=40, width=650)

        self.search_user_label = tk.Label(self.search_user_heading, text="Search User",font=("oblique", 16), bg="#a60ddc", fg="white")
        self.search_user_label.grid(row=0, column=0, pady=(4, 0))

        self.enter_username_label = tk.Label(self.search_user_detail, text="Username : ",font=("oblique", 16), bg="blue", fg="white")
        self.enter_username_label.grid(row=0, column=0, pady=(4, 0),padx=(42,0))

        self.enter_username_entry = tk.Entry(self.search_user_detail,font=("oblique", 16), bg="white")
        self.enter_username_entry.grid(row=0, column=1, pady=(0, 2))

        self.search_submit_button = tk.Button(self.search_user_detail,text="Search", font=("oblique", 16),bd=4,bg="#32cd32",justify = 'center',command = self.search_user)
        self.search_submit_button.grid(row=0, column=2, pady=(0, 0),padx=(160,0))


        self.result_after_search = tk.Frame(self.enter_detail_for_search_frame)
        self.result_after_search.place(y=80, height=254, width=650)




    def right_side_panel_third(self):
        self.make_frame_of_detail = tk.Frame(self.root,bg="#1e90ff")
        self.make_frame_of_detail.place(x=225,y=660,width=520,height=100)

        self.text_label_for_fourth_panel = tk.Label(self.make_frame_of_detail,text="Do you want to know more about\n the developer(Nitin Singh) of this software?",justify="center",bg="#1e90ff",fg="white",font=("oblique",15))
        self.text_label_for_fourth_panel.grid(row=0,padx=40)

        self.button_for_third_panel = tk.Button(self.make_frame_of_detail,text="Know more about Nitin Singh",fg="white",bg="#856d4d")
        self.button_for_third_panel.grid(row=1,padx=50,pady=10)

root = tk.Tk()

lgn = Login(root)

root.mainloop()
