from cProfile import label
from select import select
from tkinter import *
from tkinter import tk
from tkinter import messagebox
from matplotlib.cbook import is_math_text

# import new library
# to install library use following command in command prompt
# 1> pip install PyQRCode
# 2> pip install pypng

# import library
import pyqrcode
import png


root=Tk()
#title
root.title("QR code")
#icon
root.iconbitmap('qrcode.ico')
#gui logic
root.geometry("740x840")
#min/maz= width,height
root.minsize(440,440)
root.maxsize(540,540)
#label capital L
# grid(row,col),pack,place(x,y)
mess = Label(root,text="QR CODE",bg="skyblue",fg="light yellow")
mess.pack()
lb=Label(root,text="Input",fg="light yellow",bg="skyblue")
lb.pack()
#entry bottom
Var=StringVar()
ent=Entry(root,bg="grey",fg="yellow",textvariable=Var)
ent.pack()

# drop down meanu/combo box
var=StringVar()
com=ttk.Combobox(root,width=20)
com['state']= 'readonly'
com['values']=('Bussines',
                'Students',
                'payment',
                'Attendence',
                'Others')
com.pack()
com.current(0)

# Created a frame for showing qr code and name produced by rupesh
# ------------------------------- 
bottom=Frame(root)
bottom.pack(side=BOTTOM)

# Creating a label for image qrcode to show on clicking
imagelabel = Label(bottom)
imagelabel.pack()
# -----------------------------------

def func():
    if Var.get()=="":
        messagebox.showwarning("Warring","Empty input Box")
    else:
        # -----------------------
        info = Var.get() # getting value from input box
        qr = pyqrcode.create(info) # Generating qr code
        qr.png("qr.png", scale=6) # saving qrcode in file in png format
        img = PhotoImage(file = "qr.png") # Taking qrcode just saved in file to show
        imagelabel.configure(image=img) # Configuring the image label to show generated qrcode
        imagelabel.image = img # assgigning qr code to image label
        #-----------------------------
        messagebox.showinfo("success","QR Code is generated successfully.")

#button
b1=Button(root, text="Submit",bg="grey", fg="blue",command=func)
b1.pack()
#check button
# #checkbtn1=IntVar()
# checkbtn2=IntVar()
select=Checkbutton(root,text="For yourself")
select.pack()
select=Checkbutton(root,text="For Others")
select.pack()
#radio
radio_button_var = IntVar()
radio=Radiobutton(root,text="for yourself",value=1, variable=radio_button_var).pack()
radio=Radiobutton(root,text="for others",value=0, variable=radio_button_var).pack()



label=Label(bottom,text="Produce by Rupesh kumar",bg="grey",fg="blue")
label.pack(side=BOTTOM)
#image
root.mainloop()
