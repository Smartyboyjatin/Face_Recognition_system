from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img = Image.open(r"Images\11.jpeg")
        img = img.resize((800, 200))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        img1 = Image.open(r"Images\12.jpeg")
        img1 = img1.resize((800, 200))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        img3 = Image.open(
            r"Images\3.jpeg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text="ENTRY MANAGEMENT", font=("times new roman", 35, "bold"),
                          bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45,)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=52, width=1515, height=600)

        # Left Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Entry details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=760, height=500)

        img_left = Image.open(
            r"Images\12.jpeg")
        img_left = img_left.resize((745, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=130)

        Left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        Left_inside_frame.place(x=3, y=135, width=750, height=337)

        # labels and entry

        # attendance Id
        attendanceid_label = Label(Left_inside_frame, text="AttendanceId:", font=(
            "times new roman", 13, "bold"), bg="white")
        attendanceid_label.grid(row=0, column=0, padx=10, sticky=W)

        attendanceID_entry = ttk.Entry(Left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # attendance Id
        attendanceid_label = Label(Left_inside_frame, text="AttendanceId:", font=(
            "times new roman", 13, "bold"), bg="white")
        attendanceid_label.grid(row=0, column=0, padx=10, sticky=W)

        attendanceID_entry = ttk.Entry(Left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # roll no
        rolllabel=Label(Left_inside_frame, text="Roll no.:", font=(
            "times new roman", 13, "bold"), bg="white")
        rolllabel.grid(row=0, column=2, padx=4,pady=8)

        atten_roll = ttk.Entry(Left_inside_frame, width=22, font=("times new roman", 13, "bold"))
        atten_roll.grid(row=0, column=3, pady=8)

        # name
        name_label = Label(Left_inside_frame, text="Name:", font=(
            "times new roman", 13, "bold"), bg="white")
        name_label.grid(row=1, column=0)

        atten_name = ttk.Entry(Left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        atten_name.grid(row=1, column=1, pady=8)

        # department
        deplabel = Label(Left_inside_frame, text="Department:", font=(
            "times new roman", 13, "bold"), bg="white")
        deplabel.grid(row=1, column=2)

        atten_dep = ttk.Entry(Left_inside_frame, width=22, font=("times new roman", 13, "bold"))
        atten_dep.grid(row=1, column=3, pady=8)

        # time
        timelabel = Label(Left_inside_frame, text="Time:", font=(
            "times new roman", 13, "bold"), bg="white")
        timelabel.grid(row=2, column=0)

        atten_time = ttk.Entry(Left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        atten_time.grid(row=2, column=1, pady=8)

        # date
        datelabel = Label(Left_inside_frame, text="Date:", font=(
            "times new roman", 13, "bold"), bg="white")
        datelabel.grid(row=2, column=2)

        atten_date = ttk.Entry(Left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        atten_date.grid(row=2, column=3, pady=8)

        # attendance
        attendancelabel = Label(Left_inside_frame, text="Attendance Status:", font=(
            "times new roman", 13, "bold"), bg="white")
        attendancelabel.grid(row=3, column=0)

        self.atten_status=ttk.Combobox(Left_inside_frame,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)




        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Entries", font=("times new roman", 12, "bold"))
        Right_frame.place(x=780, y=10, width=720, height=500)

        # ========================== scroll bar table ===========================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable-ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=x)
        scroll_y.pack(side=RIGHT,fill=y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",Text="Attendance Id")
        self.AttendanceReportTable.heading("roll",Text="Roll no")
        self.AttendanceReportTable.heading("name",Text="Name")
        self.AttendanceReportTable.heading("department",Text="Department")
        self.AttendanceReportTable.heading("time",Text="Time")
        self.AttendanceReportTable.heading("date",Text="Date")
        self.AttendanceReportTable.heading("attendance",Text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

    # ======================= fetch data ==============================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)    

    # export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("csv File","*.csv"),("ALL File","*.*")),parent=self)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+ os.path.basename(fln)+"successfully")
                    
        except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
