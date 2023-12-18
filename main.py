from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


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

        b1 = Button(bg_img,image=self.photoimg2,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_l = Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=200,y=300,width=220,height=40)

        # Detect Face Button
        img3 = Image.open(r".\assets\Face_Detection.png")
        img3 = img3.resize((220,220),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(bg_img,image=self.photoimg3,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)

        b2_l = Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_l.place(x=500,y=300,width=220,height=40)

        # Attendance Button
        img4 = Image.open(r".\assets\Attendance.png")
        img4 = img4.resize((220,220),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b3 = Button(bg_img,image=self.photoimg4,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)

        b3_l = Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_l.place(x=800,y=300,width=220,height=40)

        # Help Button
        img5 = Image.open(r".\assets\help.png")
        img5 = img5.resize((220,220),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b4 = Button(bg_img,image=self.photoimg5,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)

        b4_l = Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_l.place(x=1100,y=300,width=220,height=40)

        # Model Training Button
        img6 = Image.open(r".\assets\Model_Training.png")
        img6 = img6.resize((220,220),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b5 = Button(bg_img,image=self.photoimg6,cursor="hand2")
        b5.place(x=200,y=380,width=220,height=220)

        b5_l = Button(bg_img,text="Model Training",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_l.place(x=200,y=580,width=220,height=40)

        # Photos Button
        img7 = Image.open(r".\assets\Photos.jpg")
        img7 = img7.resize((220,220),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b6 = Button(bg_img,image=self.photoimg7,cursor="hand2")
        b6.place(x=500,y=380,width=220,height=220)

        b6_l = Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
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

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()