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


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()