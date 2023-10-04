from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

background="#98c1d9"
framebg="#EDEDED"
framefg="#06283D"

root=Tk()
root.title("Patient's Registration Form")
root.geometry("1250x700+210+100")
root.config(bg=background)


file=pathlib.Path('Schedule_data.xlsx')
if file.exists():
    pass
else:
    file=Workbook()
    sheet=file.active
    sheet['A1']="Registration No."
    sheet['B1']="Name"
    sheet['C1']="Date of Birth"
    sheet['D1']="Gender"
    sheet['E1']="Email"
    sheet['F1']="Phone No."
    sheet['G1']="Marital Status"
    sheet['H1']="Permanent Add"
    sheet['I1']="Current Add"
    sheet['J1']="Insurance name"
    sheet['K1']="Past Medical History"
    sheet['L1']="Date of Registration"

    file.save('Patients_data.xlsx')

def Exit():
    root.destroy()



def selection():
    value=radio.get()
    if value==1:
        gender="Male"
        print(gender)
    else:
        gender="Female"
        print(gender)



#tframes
Label(root,text=" ", width=10, height=3, bg="#f0687c", anchor='e').pack(side=TOP,fill=X)
Label(root,text="PATIENTS REGISTRATION", width=10, height=2, bg="#c36464", fg='#fff', font='arial 20 bold').pack(side=TOP,fill=X)

Search=StringVar()
Entry(root,textvariable=Search, width=15, bd=2, font="arial 20").place(x=820,y=70)
imageicon3=PhotoImage(file="search.png")
Srch=Button(root,text="Search", compound=LEFT,image=imageicon3, width=123, bg='#68ddfa', font="arial 13 bold")
Srch.place(x=1060,y=66)

#imageicon4=PhotoImage(file="Layer 4.png")
#Udate_button=Button(root, image=imageicon4, bg="#c36464")
#Udate_button.place(x=110,y=64)

#reg date
Label(root,text="Registration No.:", font="arial 13", fg=framebg, bg=background).place(x=30, y=150)
#Label(root,text="Date:", font="arial 13", fg=framebg, bg=background).place(x=500, y=150)

Registration=StringVar()
Date = StringVar()
 
reg_entry = Entry(root, textvariable=Registration, width=15, font="arial 10")
reg_entry.place(x=160, y=150)

#today = date.today()
#d1 = today.strftime("%d/%m/%Y")
#date_entry = Entry(root, textvariable=Date, width=15, font="arial 10")
#date_entry.place(x=550,y=150)

#Date.set(d1)




#patients
obj=LabelFrame(root,text="Patient's Details", font=20, bd=2, width=900, bg=framebg, fg=framefg, height=250, relief=GROOVE)
obj.place(x=30, y=200)

Label(obj,text="Full Name:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=50)
Label(obj,text="Date of Birth:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=100)
Label(obj,text="Gender:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=150)

Label(obj,text="Email:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=50)
Label(obj,text="Phone No.:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=100)
Label(obj,text="Marital Status:", font="arial 13", bg=framebg, fg=framefg).place(x=500, y=150)

Name=StringVar()
name_entry = Entry(obj,textvariable=Name, width=20, font="arial 10")
name_entry.place(x=160, y=100)

DOB=StringVar()
dob_entry = Entry(obj,textvariable=DOB, width=20, font="arial 10")
dob_entry.place(x=160, y=50)

Phone=StringVar()
phone_entry = Entry(obj,textvariable=Phone, width=20, font="arial 10")
phone_entry.place(x=630, y=100)

Marital=StringVar()
marital_entry = Entry(obj,textvariable=Marital, width=20, font="arial 10")
marital_entry.place(x=630, y=150)

Email=StringVar()
email_entry = Entry(obj,textvariable=Email, width=20, font="arial 10")
email_entry.place(x=630, y=50)


radio= IntVar()
R1 = Radiobutton(obj,text="Male", variable=radio, value=1, bg=framebg, fg=framefg, command=selection)
R1.place(x=150, y=150)

R2 = Radiobutton(obj,text="Female", variable=radio, value=2, bg=framebg, fg=framefg, command=selection)
R2.place(x=200, y=150)

#patients add&history
obj2=LabelFrame(root,text="Patient's Address and Medical History", font=20, bd=2, width=900, bg=framebg, fg=framefg, height=220, relief=GROOVE)
obj2.place(x=30, y=470)

Label(obj2,text="Current Address:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=50)
Label(obj2,text="Permanent Address:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=100)

Currentaddress=StringVar()
currentaddress_entry = Entry(obj2,textvariable=Currentaddress, width=20, font="arial 10")
currentaddress_entry.place(x=195, y=50)

Peraddress=StringVar()
peraddress_entry = Entry(obj2,textvariable=Peraddress, width=20, font="arial 10")
peraddress_entry.place(x=195, y=100)

Label(obj2,text="Insurance Name:", font="arial 13", bg=framebg, fg=framefg).place(x=450, y=50)
Label(obj2,text="Past Medicla History:", font="arial 13", bg=framebg, fg=framefg).place(x=450, y=100)

Insurance=StringVar()
insurance_entry = Entry(obj2,textvariable=Insurance, width=23, font="arial 10")
insurance_entry.place(x=630, y=50)

Medicalhistory = Combobox(obj2, values=['Alcohol/Drug Abuse','Arthritis/Joint problems'
,'Asthma or Lung disease ','Blood disorder','Cancer','Dementia ','Depression/Mental illness ','Diabetes','Gastrointestinal problems','Genitourinary problems','Heart disease','High blood pressure ','High cholesterol','Liver disease','Neurological Disorder','Osteoporosis','Seizure Disorder','Stroke','Thyroid Disease','Other','Pampalipas Oras ka lang'],font="Roboto 10",width=20, state="r")
Medicalhistory.place(x=630, y=100)
Medicalhistory.set("Select Medical History")


f=Frame(root,bd=3,bg="black", width=200, height=200, relief=GROOVE)
f.place(x=1000,y=150)

img=PhotoImage(file= "upload photo.png")
lbl=Label(f,bg="black", image=img)
lbl.place(x=0,y=0)

Button(root,text="Upload",width=19, height=2, font="arial 12 bold", bg="lightblue").place(x=1000,y=370)
saveButton=Button(root,text="Save",width=19, height=2, font="arial 12 bold", bg="lightgreen")
saveButton.place(x=1000, y= 450)
Button(root,text="Reset",width=19, height=2, font="arial 12 bold", bg="lightpink").place(x=1000,y=530)
Button(root,text="Exit",width=19, height=2, font="arial 12 bold", bg="red",command=Exit).place(x=1000,y=610)


root.mainloop()