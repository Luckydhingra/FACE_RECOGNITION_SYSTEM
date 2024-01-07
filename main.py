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
		loginbtn.place(x=110, y=305, width=90, height=40)
		

		# ============= Forget Password ==================
		forgotbtn=Button(frame,command=self.forgot_password_window, text="Forget Password",cursor ="hand2",font=("times new roman",12,"bold"),borderwidth=0 , bg="darkred",fg="white", activebackground="darkred",activeforeground="white")
		forgotbtn.place(x=15, y=350, width=160,)

		# ============= New User ==================
		newregbtn=Button(frame,command=self.register_window,text="Creat New Account",cursor ="hand2",font=("times new roman",12,"bold"),borderwidth=0 , bg="darkred",fg="white", activebackground="darkred",activeforeground="white")
		newregbtn.place(x=15, y=385, width=160,)

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
				open_main=messagebox.askyesno("Yes NO", "Access Only Admin")
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


			
					
class Register:
	def __init__(self, root):
		self.root = root
		self.root.title("Register")
		self.root.iconbitmap('assets/logo_PI6_icon.ico')
		self.root.geometry("1500x800+0+0")

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

		# =============bg assets ===============
		self.bg=ImageTk.PhotoImage(file="assets/asus-zenbook.jpg")
		bg_lbl = Label(self.root, image=self.bg, bg='black', height=100, width=100)
		



		
		# ============== frame =================
		frame = Frame(self.root, bg='black', width=760,height=555)
		frame.place(x=385, y=100)

		# ===============Register Form ===============

		register_lbl=Label(frame,text='REGISTER HERE',font=('times new roman',25,'bold'),fg='darkgreen',bg='black')
		register_lbl.place(x=220,y=20)

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
				messagebox.showinfo("Success","Register Succesfully , Back to Login page.")
				conn.close()
   
                            


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Face Recognition System")

        # Header Image
        img = Image.open(r".\assets\Header.png")
        img = img.resize((1540,130),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1540,height=130)

        # Background Image
        img1 = Image.open(r".\assets\Background.jpg")
        img1 = img1.resize((1540,660),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0,y=130,width=1540,height=660)

        title_lbl = Label(bg_img,text="STUDENT ATTENDANCE MONITORING SYSTEM USING FACE RECOGNITION",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1540,height=45) 

        # Student Details Button
        img2 = Image.open(r".\assets\Students.png")
        img2 = img2.resize((220,220),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(bg_img,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_l = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=200,y=300,width=220,height=40)

        # Detect Face Button
        img3 = Image.open(r".\assets\Face_Detection.png")
        img3 = img3.resize((220,220),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(bg_img,image=self.photoimg3,cursor="hand2", command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_l = Button(bg_img,text="Face Detector",cursor="hand2", command=self.face_data, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_l.place(x=500,y=300,width=220,height=40)

        # Attendance Button
        img4 = Image.open(r".\assets\Attendance.png")
        img4 = img4.resize((220,220),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b3 = Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=220,height=220)

        b3_l = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_l.place(x=800,y=300,width=220,height=40)

        # Help Button
        img5 = Image.open(r".\assets\help.png")
        img5 = img5.resize((220,220),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b4 = Button(bg_img,image=self.photoimg5,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)

        b4_l = Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_l.place(x=1100,y=300,width=220,height=40)

        # Training the Algorithm Button
        img6 = Image.open(r".\assets\Model_Training.png")
        img6 = img6.resize((220,220),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b5 = Button(bg_img,image=self.photoimg6,cursor="hand2", command=self.train_algo)
        b5.place(x=200,y=380,width=220,height=220)

        b5_l = Button(bg_img,text="Algorithm Training",cursor="hand2", command=self.train_algo,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_l.place(x=200,y=580,width=220,height=40)

        # Photos Button
        img7 = Image.open(r".\assets\Photos.jpg")
        img7 = img7.resize((220,220),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b6 = Button(bg_img,image=self.photoimg7,cursor="hand2", command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6_l = Button(bg_img,text="Photos",cursor="hand2", command=self.open_img, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_l.place(x=500,y=580,width=220,height=40)

        # Developers Button
        img8 = Image.open(r".\assets\developer.png")
        img8 = img8.resize((220,220),Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b7 = Button(bg_img,image=self.photoimg8,cursor="hand2")
        b7.place(x=800,y=380,width=220,height=220)

        b7_l = Button(bg_img,text="Developers",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_l.place(x=800,y=580,width=220,height=40)

        # Exit Button
        img9 = Image.open(r".\assets\exit.png")
        img9 = img9.resize((220,220),Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b8 = Button(bg_img,image=self.photoimg9,cursor="hand2")
        b8.place(x=1100,y=380,width=220,height=220)

        b8_l = Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_l.place(x=1100,y=580,width=220,height=40)
    
    def open_img(self):
        os.startfile("data")

    # Buttons functions
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train_algo(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = LoginWindow(root)
    root.mainloop()