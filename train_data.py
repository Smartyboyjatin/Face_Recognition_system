from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"),
                          bg="skyblue", fg="darkblue")  
        title_lbl.place(x=0, y=0, width=1530, height=45,)


        img_Top = Image.open(r"Images\5.jpeg")
        img_Top = img_Top.resize((1530, 325))
        self.photoimg_Top = ImageTk.PhotoImage(img_Top)

        f_lbl = Label(self.root, image=self.photoimg_Top)
        f_lbl.place(x=0, y=45, width=1530, height=325)

        # button
        b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2", font=(
            "times new roman", 30, "bold"), bg="blue", fg="white")
        b1_1.place(x=0, y=370, width=1530, height=70)


        img_bottom = Image.open(
            r"Images\7.jpeg")
        img_bottom = img_bottom.resize((1530, 325))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)



    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ============== Train the classifier And save =====================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")








if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
