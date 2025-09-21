from tkinter import *
import  mysql.connector


db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Buji@1998",
        database = "employee"

)
mycursor = db.cursor()

class databases:
    pass




window = Tk()
window.geometry("400x450")

frame = Frame(window)
frame.pack(anchor=NW)

id= Label(frame,text="ID :")
id.grid(row=0,column=0,padx=20,pady=15)

id1 = Entry(frame,width=30)
id1.grid(row=0,column=1)

name = Label(frame,text="NAME :")
name.grid(row=1,column=0,padx=20,pady=15)

name1 = Entry(frame,width=30)
name1.grid(row=1,column=1)

dob = Label(frame,text="DATE OF BIRTH :")
dob.grid(row=2,column=0,padx=20,pady=15)

dob1 = Entry(frame,width=30)
dob1.grid(row=2,column=1)

DOJ = Label(frame,text="DATE OF JOIN :")
DOJ.grid(row=3,column=0,padx=20,pady=15)

DOJ1 = Entry(frame,width=30)
DOJ1.grid(row=3,column=1)

DEPARTMENT = Label(frame,text="DEPARTMENT :")
DEPARTMENT.grid(row=4,column=0,padx=20,pady=15)

DEPARTMENT1 = Entry(frame,width=30)
DEPARTMENT1.grid(row=4,column=1)

frame2 = Frame(window,)
frame2.pack()

submit = Button(frame2,text = "SUBMIT",
                width=15,
                )
submit.grid(row=0,column=0,padx= 5 ,pady= 10)

ADD = Button(frame2,text = "ADD",
                width=15,
                )
ADD.grid(row=0,column=1,padx= 5 ,pady= 10)

update = Button(frame2,text = "UPDATE",
                width=15,
                )
update.grid(row=0,column=2,padx= 5 ,pady= 10)

delete = Button(frame2,text = "DELETE",
                width=15,
                )
delete.grid(row=1,column=0,padx= 5 ,pady= 10)

search = Button(frame2,text = "SEARCH",
                width=15,
                )
search.grid(row=1,column=1,padx= 5 ,pady= 10)

window.mainloop()



