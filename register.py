from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

class Register:
	def __init__(self, root):
		self.root = root
		self.root.title("Register")
		self.root.iconbitmap('assets/logo_PI6_icon.ico')
		self.root.geometry("1500x800+0+0")
		

		bg_image =Image.open("assets/Banner2.jpg")		
		bg_image =bg_image.resize((1800,1100),Image.Resampling.LANCZOS)
		self.bg_image=ImageTk.PhotoImage(bg_image)
		bg=Label(self.root,image=self.bg_image)
		bg.place(x=0,y=0,relwidth=1,relheight=1)
		# =========================== Variables ===========
		self.var_fname=StringVar()
		self.var_lname=StringVar()
		self.var_contact=StringVar()
		self.var_email=StringVar()
		self.var_securityQ=StringVar()
		self.var_SecrityA=StringVar()
		self.var_pass=StringVar()
		self.var_confpass=StringVar()
		self.var_check=IntVar()
 
		# ============== frame =================
		frame = Frame(self.root, bg='black', width=760,height=555)
		frame.place(x=385, y=100)

		# ===============Register Form ===============

		register_lbl=Label(frame,text='REGISTER HERE',font=('times new roman',20,'bold'),fg='red',bg='white')
		register_lbl.place(x=260,y=25)

		# ============Label and Entry ==============

		fname=Label(frame,text='First Name',font=('times new roman',15,'bold'),fg='white',bg='black')
		fname.place(x=80, y=80)
		fname_entry=ttk.Entry(frame, textvariable=self.var_fname, font=('times new roman',15,'bold'))
		fname_entry.place(x=80,y=110,width=250)

		lname=Label(frame,text='Last Name',font=('times new roman',15,'bold'),fg='white',bg='black')
		lname.place(x=420, y=80)
		lname_entry=ttk.Entry(frame, textvariable=self.var_lname, font=('times new roman',15,'bold'))
		lname_entry.place(x=420,y=110,width=250)

		# =============== 2nd Row =====================
		contact=Label(frame,text='Contact No.',font=('times new roman',15,'bold'),fg='white',bg='black')
		contact.place(x=80, y=150)
		contact_entry=ttk.Entry(frame, textvariable=self.var_contact, font=('times new roman',15,'bold'))
		contact_entry.place(x=80,y=180,width=250)

		email=Label(frame,text='Email',font=('times new roman',15,'bold'),fg='white',bg='black')
		email.place(x=420, y=150)
		email_entry=ttk.Entry(frame, textvariable=self.var_email, font=('times new roman',15,'bold'))
		email_entry.place(x=420,y=180,width=250)

		# ================ 3rd Row ==============
		secur_que=Label(frame,text='Select Security Questions',font=('times new roman',15,'bold'),fg='white',bg='black')
		secur_que.place(x=80, y=220)
		secur_que_entry=ttk.Combobox(frame, textvariable=self.var_securityQ, font=('times new roman',13,'bold'))
		secur_que_entry['state']='readonly'
		secur_que_entry['values']=('Select Your Security Questions',
									'What is your Birth date?',
									'What is your Birth place?',
									'What is your Girlfried name?',
									'What is your Father name?',
									'What is your Mother name?',
									'What is your pet name?',
									'What is your favrite game?',
									)
		secur_que_entry.current(0)
		secur_que_entry.place(x=80,y=250,width=250)

		secure_ans=Label(frame,text='Security Answer',font=('times new roman',15,'bold'),fg='white',bg='black')
		secure_ans.place(x=420, y=220)
		secure_ans_entry=ttk.Entry(frame, textvariable=self.var_SecrityA, font=('times new roman',15,'bold'))
		secure_ans_entry.place(x=420,y=250,width=250)

		# ==================== 4th Row ===============================
		passwd=Label(frame,text='Password',font=('times new roman',15,'bold'),fg='white',bg='black')
		passwd.place(x=80, y=290)
		passwd_entry=ttk.Entry(frame, textvariable=self.var_pass, font=('times new roman',15,'bold'))
		passwd_entry.place(x=80,y=320,width=250)

		confirm_passwd=Label(frame,text='Confirm Password',font=('times new roman',15,'bold'),fg='white',bg='black')
		confirm_passwd.place(x=420, y=290)
		confirm_passwd_entry=ttk.Entry(frame, textvariable=self.var_confpass, font=('times new roman',15,'bold'))
		confirm_passwd_entry.place(x=420,y=320,width=250)

		# =================== 5th row Check Button =================================
		checkbtn=Checkbutton(frame,variable=self.var_check, text="I Agree the Terms & Conditions",bg='black', fg='blue', font=('times new roman',13,'bold'), onvalue=1, offvalue=0)
		checkbtn.place(x=80, y=360)


		# ==================== Buttons =================================================

		img=Image.open("assets/Register1.png")
		img=img.resize((200,50),Image.Resampling.LANCZOS)
		self.photoimage=ImageTk.PhotoImage(img)
		reg=Button(frame,command=self.register_data, image=self.photoimage,borderwidth=0, cursor='hand2',bg='black', fg='black',font=('times new roman',13,'bold'))
		reg.place(x=250, y=450)

		


		# ============== function Declaration ==============================
	def register_data(self):
		if self.var_fname.get()=="":
			messagebox.showerror("Required","First Name is Required.")
		elif self.var_lname.get()=="":
			messagebox.showerror("Required","Last Name is Required.")
		elif self.var_email.get()=="":
			messagebox.showerror("Required","Email is Required.\nFor Example: username12@gmail.com")
		elif self.var_securityQ.get()=="Select Your Security Questions":
		  messagebox.showerror("Error","Select your Security Questions.")
		elif self.var_SecrityA.get()=="":
			messagebox.showerror("Required","Security Answer is Required.")
		elif self.var_pass.get()=="":
			messagebox.showerror("Required","Password is Required.")
		elif self.var_pass.get()!=self.var_confpass.get():
			messagebox.showerror("Error","Password and Confirm Password must be same.")
		elif self.var_check.get()==0:
			messagebox.showerror("Error","Please agree our Terms and Condition.")
		else:
			conn=mysql.connector.connect(host='localhost',user='root',password='4321',database='student_database',auth_plugin='mysql_native_password')
			reg_cursor=conn.cursor()
			query=("select * from register where email=%s")
			value=(self.var_email.get(),)
			reg_cursor.execute(query,value)
			row=reg_cursor.fetchone()
			if row!=None:
				messagebox.showerror("Error","User already exist,\nPlease try another email.")
			else:
				reg_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
					self.var_fname.get(),
					self.var_lname.get(),
					self.var_contact.get(),
					self.var_email.get(),
					self.var_securityQ.get(),
					self.var_SecrityA.get(),
					self.var_pass.get(),
				))
			
			if row!=None:
				messagebox.showwarning("Change","Change your email")
			else:
				conn.commit()
				messagebox.showinfo("Success","Register Succesfully.")
				conn.close()
if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()    