from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
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
        img1 = img1.resize((1540,710),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0,y=130,width=1540,height=710)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1540,height=45)

        # Main Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1490, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 13, "bold"))
        Left_frame.place(x=15, y=10, width=760, height=580)

        img_left = Image.open(r".\assets\collegestudents.jpg")
        img_left = img_left.resize((750,130),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=130)

        # current course information
        currentCourse_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 13, "bold"))
        currentCourse_frame.place(x=5, y=135, width=750, height=115)

        # Department
        dep_label = Label(currentCourse_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(currentCourse_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department","CSE","CSE (AI & ML)","Civil","Mechanical", "Electrical","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(currentCourse_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(currentCourse_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course","B.Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #  Year
        year_label = Label(currentCourse_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(currentCourse_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year","2023-24","2024-25","2025-26","2026-27")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(currentCourse_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(currentCourse_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student information
        classStudent_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 13, "bold"))
        classStudent_frame.place(x=5, y=250, width=750, height=300)

        # Registration No.
        regNo_label = Label(classStudent_frame, text="Registration No:", font=("times new roman", 13, "bold"), bg="white")
        regNo_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        regNo_entry = ttk.Entry(classStudent_frame, width=20, font=("times new roman", 13, "bold"))
        regNo_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(classStudent_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(classStudent_frame, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        classDiv_label = Label(classStudent_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        classDiv_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        classDiv_entry = ttk.Entry(classStudent_frame, width=20, font=("times new roman", 13, "bold"))
        classDiv_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No.
        rollNo_label = Label(classStudent_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        rollNo_entry = ttk.Entry(classStudent_frame, width=20, font=("times new roman", 13, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(classStudent_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_entry = ttk.Entry(classStudent_frame, width=20, font=("times new roman", 13, "bold"))
        gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(classStudent_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(classStudent_frame, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(classStudent_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(classStudent_frame, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No.
        phone_label = Label(classStudent_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(classStudent_frame, width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(classStudent_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(classStudent_frame, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(classStudent_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(classStudent_frame, width=20, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio Buttons
        radiobtn1 = ttk.Radiobutton(classStudent_frame,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2 = ttk.Radiobutton(classStudent_frame,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # buttons Frame 
        btn_frame = Frame(classStudent_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=745, height=35)

        save_btn = Button(btn_frame, text="Save",width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # buttons Frame 1
        btn_frame1 = Frame(classStudent_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=745, height=35)

        takePhoto_btn = Button(btn_frame1, text="Take Photo Sample",width=37, font=("times new roman",13,"bold"), bg="blue", fg="white")
        takePhoto_btn.grid(row=0, column=0)

        updatePhoto_btn = Button(btn_frame1, text="Update Photo Sample",width=37, font=("times new roman",13,"bold"), bg="blue", fg="white")
        updatePhoto_btn.grid(row=0, column=1)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 13, "bold"))
        Right_frame.place(x=790, y=10, width=670, height=580)

        img_right = Image.open(r".\assets\collegestudents1.jpg")
        img_right = img_right.resize((660,130),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=660,height=130)

        # fetching Student details
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search student details", font=("times new roman", 13, "bold"))
        search_frame.place(x=5, y=135, width=660, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select","Roll No.","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search",width=10, font=("times new roman",12,"bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text="Show All",width=10, font=("times new roman",12,"bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=660, height=340)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep","course","year","sem","roll","reg_no","name","div","dob","gender","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # "dep","course","year","sem","roll","reg_no","name","div","dob","gender","email","phone","address","teacher","photo"
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("reg_no",text="Registration No.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("reg_no",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()