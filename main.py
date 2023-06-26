from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train_data import Train
from face_detector import Face_recognition
from attendance import Attendance
import os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Invertis University")

        # first Image
        img = Image.open(
            r"Images\20.jpeg")
        img = img.resize((510, 160))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=510, height=160)

        # second Image
        img1 = Image.open(
            r"Images\1.jpeg")
        img1 = img1.resize((510, 170))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=510, y=0, width=510, height=160)

        # third Image
        img2 = Image.open(
            r"Images\2.jpeg")
        img2 = img2.resize((510, 160))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1020, y=0, width=510, height=160)

        # background Image
        img3 = Image.open(
            r"Images\invertis.jpg")
        img3 = img3.resize((1530, 666))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # main Title
        title_lbl = Label(bg_img, text="FACE RECOGNITION LIBRARY ENTRY SYSTEM", font=("times new roman", 35, "bold"),
                          bg="red", fg="white")
        title_lbl.place(x=-3, y=-2, width=1530, height=45)

        # Student part
        img4 = Image.open(
            r"Images\23.jpg")
        img4 = img4.resize((300, 250))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand2")
        b1.place(x=80, y=210, width=230, height=230)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.place(x=80, y=445, width=230, height=40)


        # Train data part
        img6 = Image.open(
            r"Images\19.jpeg")
        img6 = img6.resize((300, 270))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6,
                    cursor="hand2",command=self.train_data )
        b3.place(x=360, y=210, width=230, height=230)

        b3_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data ,font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        b3_1.place(x=360, y=445, width=230, height=40)

        # Face Detector part
        img5 = Image.open(
            r"Images\14.jpeg")
        img5 = img5.resize((370, 270))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5,
                    cursor="hand2", command=self.face_detector)
        b2.place(x=640, y=210, width=230, height=230)

        b2_1 = Button(bg_img, text="Scanner", cursor="hand2",command=self.face_detector, font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        b2_1.place(x=640, y=445, width=230, height=40)

        # Photo face part
        img7 = Image.open(
            r"Images\29.jpg")
        img7 = img7.resize((270, 270))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7,
                    cursor="hand2",command=self.open_img )
        b4.place(x=920, y=210, width=230, height=230)

        b4_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img , font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        b4_1.place(x=920, y=445, width=230, height=40)

        # Record part
        img8 = Image.open(
            r"Images\28.jpg")
        img8 = img8.resize((250, 230))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8,
                    cursor="hand2",command=self.attendance_data)
        b5.place(x=1200, y=210, width=230, height=230)

        b5_1 = Button(bg_img, text="Entry Record", cursor="hand2",command=self.attendance_data,font=(
            "times new roman", 20, "bold"), bg="blue", fg="white")
        b5_1.place(x=1200, y=445, width=230, height=40)




    # ================================= Function Buttons ==================================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_detector(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)    

    def open_img(self):
        os.startfile("data")







# class object creation
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
