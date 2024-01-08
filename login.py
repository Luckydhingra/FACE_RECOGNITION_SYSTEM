from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from register import Register
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
	win=Tk()
	app=LoginWindow(win)
	win.mainloop()


class LoginWindow:
	def __init__(self, root):
		self.root=root
		self.root.title("Login")
		self.root.iconbitmap('assets/logo_PI6_icon.ico')
		self.root.geometry("1500x800+0+0")
  
		bg_image =Image.open("assets/Banner2.jpg")		
		bg_image =bg_image.resize((1800,1100),Image.Resampling.LANCZOS)
		self.bg_image=ImageTk.PhotoImage(bg_image)
		bg=Label(self.root,image=self.bg_image)
		bg.place(x=0,y=0,relwidth=1,relheight=1)

		frame=Frame(self.root,bg="black")
		frame.place(x=610,y=170,width=340,height=450)

		img1=Image.open("assets/r.png")
		img1=img1.resize((100,100),Image.Resampling.LANCZOS)
		self.photoimage1=ImageTk.PhotoImage(img1)
		lblimg1=Label(image=self.photoimage1,bg="black", borderwidth=0)
		lblimg1.place(x=730,y=175,width=100,height=100)

		get_str=Label(frame,text="Get Started", font=("times new roman",20,"bold"),fg="white",bg="black")
		get_str.place(x=95,y=100)

		# label for Username
		username=lbl=Label(frame,text="Username/Email", font=("times new roman",15,"bold"),fg="white",bg="black")
		username.place(x=70,y=155)

		self.textuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
		self.textuser.place(x=40,y=185,width=270)

		# Label for Password
		password=lbl=Label(frame,text="Password", font=("times new roman",15,"bold"),fg="white",bg="black")
		password.place(x=70,y=225)

		self.textpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
		self.textpass.place(x=40,y=255,width=270)

		# ======== Icon assets ===================================
		img2=Image.open("assets/r.png")
		img2=img2.resize((25,25),Image.Resampling.LANCZOS)
		self.photoimage2=ImageTk.PhotoImage(img2)
		lblimg2=Label(image=self.photoimage2,bg="black", borderwidth=0)
		lblimg2.place(x=650,y=325,width=25,height=25)
	
		img3=Image.open("assets/lock.png")
		img3=img3.resize((25,25),Image.Resampling.LANCZOS)
		self.photoimage3=ImageTk.PhotoImage(img3)
		lblimg3=Label(image=self.photoimage3,bg="black", borderwidth=0)
		lblimg3.place(x=650,y=395,width=25,height=25)

		# Login button
		loginbtn=Button(frame, command=self.login, text="Login",cursor ="hand2",font=("times new roman",15,"bold"),bd=5,relief=RIDGE,bg="darkblue",fg="white", activebackground="darkblue",activeforeground="white")
		loginbtn.place(x=125, y=305, width=90, height=40)
		

		# ============= Forget Password ==================
		forgotbtn=Button(frame,command=self.forgot_password_window, text="Forget Password",cursor ="hand2",font=("times new roman",12,"bold"),borderwidth=0 , bg="darkred",fg="white", activebackground="darkred",activeforeground="white")
		forgotbtn.place(x=15, y=360, width=160,)

		# ============= New User ==================
		newregbtn=Button(frame,command=self.register_window,text="Creat New Account",cursor ="hand2",font=("times new roman",12,"bold"),borderwidth=0 , bg="darkred",fg="white", activebackground="darkred",activeforeground="white")
		newregbtn.place(x=15, y=395, width=160,)

	# ======== function ==========
	def register_window(self):
		self.new_window=Toplevel(self.root)
		self.app=Register(self.new_window)

	def login(self):
		if self.textuser.get()=="" or self.textpass.get()=="":
			messagebox.showerror("Error", "All Field are Required")
		else:
			conn=mysql.connector.connect(host='localhost',user='root',password='4321',database='student_database',auth_plugin='mysql_native_password')
			reg_cursor=conn.cursor()
			reg_cursor.execute("select * from register where email=%s and pass=%s",(
																						self.textuser.get(),
																						self.textpass.get()
																						))
			
			row=reg_cursor.fetchone()
			if row==None:
				messagebox.showerror("Error", "Invalid Username and Password.")
			else:
				open_main=messagebox.askyesno("Admin", "Access Only Admin")
				if open_main>0:
						self.new_window=Toplevel(self.root)
						self.app=Face_Recognition_System(self.new_window)
				else:
					if not open_main:
						return
			conn.commit()
			conn.close()
			
	# ======== Reset Password function ====================
	def reset_pass(self):
		if self.combo_securiy_Q.get()=="Select Your Security Questions":
			messagebox.showerror("Error", "Please Select Your Security Questions.",parent=self.root2)
		elif self.txt_security.get()=="":
			messagebox.showwarning("Warning", "Please Enter The Answer.",parent=self.root2)
		elif self.txt_newpass.get()=="":
			messagebox.showwarning("Warning", "Please Enter The New Password.",parent=self.root2)
		else:
			conn=mysql.connector.connect(host='localhost',user='root',password='4321',database='student_database',auth_plugin='mysql_native_password')
			reg_cursor=conn.cursor()
			qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
			value=(self.textuser.get(),self.combo_securiy_Q.get(),self.txt_security.get())
			reg_cursor.execute(qury,value)
			row=reg_cursor.fetchone()
			if row==None:
				messagebox.showwarning("Warning", "Please Enter The Correct Answer.",parent=self.root2)
			else:
				query=("update register set pass=%s where email=%s")
				value=(self.txt_newpass.get(),self.textuser.get())
				reg_cursor.execute(query,value)

				conn.commit()
				conn.close()
				messagebox.showinfo("Info", "Your Password has been reset Successfully, \n Please Login with New Password.",parent=self.root2)
				self.root2.destroy()


	# ============================= Forgot Password Windows =========================
	def forgot_password_window(self):
		if self.textuser.get()=="":
			messagebox.showerror("Error", "Please Enter The Email Address To Reset Password")
		else:
			conn=mysql.connector.connect(host='localhost',user='root',password='4321',database='student_database',auth_plugin='mysql_native_password')
			reg_cursor=conn.cursor()
			query=("select * from register where email=%s")
			value=(self.textuser.get(),)
			reg_cursor.execute(query, value)
			row=reg_cursor.fetchone()

			if row==None:
				messagebox.showerror("Error", "Please Enter The Valid Username/Email name.")
			else:
				conn.close()
				self.root2=Toplevel()
				self.root2.title("Forget Password")
				self.root2.iconbitmap('assets/logo_PI6_icon.ico')
				self.root2.geometry("340x450+610+170")

				fglbl=Label(self.root2, text="Forget Password", font=("times new roman",18,"bold"),bg="black",fg="red")
				fglbl.place(x=0,y=10,relwidth=1)

				# ================ forgot password Row ==============
				security_Q=Label(self.root2,text='Select Security Questions',font=('times new roman',15,'bold'),fg='black')
				security_Q.place(x=50, y=80)
				
				self.combo_securiy_Q=ttk.Combobox(self.root2,  font=('times new roman',13,'bold'))
				self.combo_securiy_Q['state']='readonly'
				self.combo_securiy_Q['values']=('Select Your Security Questions',
											'What is your Birth date?',
											'What is your Birth place?',
											'What is your Girlfried name?',
											'What is your Father name?',
											'What is your Mother name?',
											'What is your pet name?',
											'What is your favrite game?',
											)
				self.combo_securiy_Q.current(0)
				self.combo_securiy_Q.place(x=50,y=110,width=250)

				security_A=Label(self.root2,text='Security Answer',font=('times new roman',15,'bold'),fg='black')
				security_A.place(x=50, y=150)
				
				self.txt_security=ttk.Entry(self.root2,  font=('times new roman',15,'bold'))
				self.txt_security.place(x=50,y=180,width=250)

				new_password=Label(self.root2,text='New Password',font=('times new roman',15,'bold'),fg='black')
				new_password.place(x=50, y=220)
				
				self.txt_newpass=ttk.Entry(self.root2,  font=('times new roman',15,'bold'))
				self.txt_newpass.place(x=50,y=250,width=250)

				btn=Button(self.root2, command=self.reset_pass, text="Reset",font=("times new roman",15,"bold"),bd=5,fg="white",bg="green")
				btn.place(x=100,y=290)


			
					

if __name__ == "__main__":
    root = Tk()
    obj = LoginWindow(root)
    root.mainloop()    