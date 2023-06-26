from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"),
                          bg="darkblue", fg="orange")
        title_lbl.place(x=0, y=0, width=1530, height=45,)

        # First image
        img_Top = Image.open(
            r"Images\26.jpg")
        img_Top = img_Top.resize((850, 700))
        self.photoimg_Top = ImageTk.PhotoImage(img_Top)

        f_lbl = Label(self.root, image=self.photoimg_Top)
        f_lbl.place(x=0, y=45, width=850, height=700)

        # second image
        img_bottom = Image.open(
            r"Images\25.jpg")
        img_bottom = img_bottom.resize((950, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=850, y=45, width=680, height=700)

        b1_1 = Button(f_lbl, text="START SCANNING", cursor="hand2", font=(
            "times new roman", 18, "bold"), bg="blue", fg="white")
        b1_1.place(x=133, y=630, width=415, height=55)

    # =============================== attendance =====================================================

    def mark_attendance(self,i,r,n,d):
        with open("Entry.csv",newline="\n") as f:
            myDataList=f.readlines()
            name_List=[]
            for line in myDataList:
                entry=line.split((","))
                name_List.append(entry[0])
            if((i not in name_List) and (r not in name_List) and (n not in name_List) and (d not in name_List)):
                now =datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1}")




    # ================== face recognition ====================================

    def face_recognition(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x+w, y+h), (0, 255, 0), 3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Ar1122@my", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id"+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id"+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id"+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Dep from student where Student_id"+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)


                if confidence > 77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            
            return coord    
            
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("")
        clf=cv2.face.LBPHFaceRecognizer_craete()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face Recognition",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()




if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
