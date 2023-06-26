from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        ################### VARIABLE #################################

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        img = Image.open(
            r"Images\11.jpeg")
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        img1 = Image.open(
            r"Images\12.jpeg")
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        img2 = Image.open(
            r"Images\17.jpeg")
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        img3 = Image.open(
            r"Images\3.jpeg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENTS DETAILS", font=("times new roman", 35, "bold"),
                          bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45,)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=55, width=1500, height=600)

        # Left Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)

        img_left = Image.open(
            r"Images\12.jpeg")
        img_left = img_left.resize((745, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=130)

        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=745, height=115)

        # department
        dep_label = Label(current_course_frame, text="Department", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, font=(
            "times new roman", 12, "bold"), state="read only", width=20)
        dep_combo["values"] = ("select Department",
                               "Computer", "IT", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, font=(
            "times new roman", 12, "bold"), state="read only", width=20)
        course_combo["values"] = (
            "select Course", "EE", "CS", "SE", "BE", "ME")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        year_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, font=(
            "times new roman", 12, "bold"), state="read only", width=20)
        year_combo["values"] = ("select Year", "2020", "2021", "2022",
                                "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semetser
        semester_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"), state="read only", width=20)
        semester_combo["values"] = (
            "select Semester", "Computer", "IT", "Mechanical")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Current Course Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=745, height=300)

        studentid_label = Label(class_student_frame, text="StudentID:", font=(
            "times new roman", 13, "bold"), bg="white")
        studentid_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        studentName_label = Label(class_student_frame, text="StudentName", font=(
            "times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        class_div_label = Label(class_student_frame, text="Class Division:", font=(
            "times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        roll_no_label = Label(class_student_frame, text="Roll No:", font=(
            "times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        email_label = Label(class_student_frame, text="Email Id:", font=(
            "times new roman", 13, "bold"), bg="white")
        email_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, width=20, font=(
            "times new roman", 13, "bold"))
        email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Gender_label = Label(class_student_frame, text="Gender:", font=(
            "times new roman", 13, "bold"), bg="white")
        Gender_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        Gender_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold"))
        Gender_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        dob_label = Label(class_student_frame, text="DOB:", font=(
            "times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, width=20,
                              font=("times new roman", 13, "bold"))
        dob_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        phone_label = Label(class_student_frame, text="Phone No:", font=(
            "times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, width=20, font=(
            "times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        address_label = Label(class_student_frame, text="Address:", font=(
            "times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        TecherName_label = Label(class_student_frame, text="Teacher Name:", font=(
            "times new roman", 13, "bold"), bg="white")
        TecherName_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        TecherName_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold"))
        TecherName_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        radiobtn1 = ttk.Radiobutton(
            class_student_frame, text="Take photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame, text="No photo Sample", value="Yes")
        radiobtn2.grid(row=5, column=1)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=780, y=10, width=700, height=580)

        img_right = Image.open(
            r"Images\13.jpeg")
        img_right = img_right.resize((720, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        ##################        search system        ##############################

        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(Search_frame, text="Search by:", font=(
            "times new roman", 15, "bold"), bg="red")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=(
            "times new roman", 12, "bold"), state="read only", width=20)
        search_combo["values"] = ("select", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_entry = ttk.Entry(
            Search_frame, width=15, font=("times new roman", 13, "bold"))
        Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search", width=11, font=(
            "Times now roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(Search_frame, text="Show All", width=11, font=(
            "Times now roman", 13, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=('dep', 'course', 'year', 'sem', 'id', 'name', 'div', 'roll no', 'gender',
                                          'dob', 'email', 'phone', 'address', 'teacher', 'photo'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll no", text="Roll no")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Dob")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll no", width=100)
        self.student_table.column("gender", width=100)

        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        ##################### FUNCTION DECLARATION #########################

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Jatin@2509", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into student entry record values(%s,%s,%s,%s)", (

                    self.var_std_id.get(),
                    self.var_course.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    # self.var_year.get(),
                    # self.var_semester.get(),
                    # self.var_div.get(),
                    # self.var_gender.get(),
                    # self.var_dob.get(),
                    # self.var_email.get(),
                    # self.var_phone.get(),
                    # self.var_address.get(),
                    # self.var_teacher.get(),
                    # self.var_radio1.get()


                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "success", "student details  has been added", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Ar1122@my", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:

                self.student_table.insert("", END, values=i)

            conn.commit()
        conn.close()

        # get cursor #####################3

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

        ######### update function ###########

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)

        else:
            try:
                Upadate = messagebox.askyesno(
                    "Update", "Do you want to update data", parent=self.root)
                if Upadate > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Ar1122@my", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (



                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()


                    ))

                else:
                    if not Upadate:
                        return
                messagebox.showinfo(
                    "Success", "Student details successfully update complete", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
