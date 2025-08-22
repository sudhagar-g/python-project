from tkinter import *


def button_press(num):
    global  sum_text
    sum_text = sum_text + str(num)
    output_label.set(sum_text)

def equation():
    global sum_text

    try:

          total = str(eval(sum_text))
          output_label.set(total)
          sum_text = total
          

    except SyntaxError:
         output_label.set("syntax error") 
         sum_text =""   

    except ZeroDivisionError:
         output_label.set("Cannot divide by zero")
         sum_text =""

              


def clear():
     global sum_text
     output_label.set("")
     sum_text = ""


    

root = Tk()
root.title("CALCULATOR")
cals_image = PhotoImage(file='C:\\project_git\\GUI\\image\\calculater.png')

root.iconphoto(True,cals_image)
root.geometry("320x420")
root.config(background='#383535')

sum_text = ""
output_label = StringVar()

label = Label(root,
              textvariable=output_label,
              font=('console',20),
              bg='white',
              width=19,
              height=2
              )
label.pack(pady=10)

frame = Frame(root)
frame.pack()

button7 = Button(frame,
                 text=7,
                 width=8,
                 height=3,
                 font=35,
                 command=lambda:button_press(7)
                 )
button7.grid(row=0,column=0)

button8 = Button(frame,
                 text=8,
                 width=8,
                 height=3,
                 font=35,
                 command=lambda:button_press(8)
                 )
button8.grid(row=0,column=1)

button9 = Button(frame,
                 text=9,
                 width=8,
                 height=3,
                 font=35,
                 command=lambda:button_press(9)
                 )
button9.grid(row=0,column=2)

button6 = Button(frame,
                 text=6,
                 width=8,
                 height=3,
                 font=35,
                 command=lambda:button_press(6)
                 )
button6.grid(row=1,column=2)

button5 = Button(frame,
                 text=5,
                 width=8,
                 height=3,
                 font=35,
                 command=lambda:button_press(5)
                 )
button5.grid(row=1,column=1)

button4 = Button(frame,
                 text=4,
                 width=8,
                 height=3,
                 font=35,
                 command=lambda:button_press(4)
                 )
button4.grid(row=1,column=0)

button3 = Button(frame,
                 text=3,
                 width=8,
                 height=3,
                 font=35,
                 command=lambda:button_press(3)
                 )
button3.grid(row=2,column=2)

button2 = Button(frame,
                 text=2,
                 width=8,
                 height=3,
                 font=35,
                 command=lambda:button_press(2)
                 )
button2.grid(row=2,column=1)

button1 = Button(frame,
                 text=1,
                 width=8,
                 height=3,
                 font=35,
                 command=lambda:button_press(1)
                 )
button1.grid(row=2,column=0)

button0 = Button(frame,
                 text=0,
                 width=8,
                 height=3,
                 font=35,
                 command=lambda:button_press(0)
                 )
button0.grid(row=3,column=1)

buttonDot = Button(frame,
                 text=".",
                 width=8,
                 height=3,
                 font=35,
                 command=lambda:button_press(".")
                 )
buttonDot.grid(row=3,column=0)

buttonPlus = Button(frame,
                    text= "+",
                    width=8,
                    height=3,
                    font=35,
                    command=lambda:button_press('+')
                        )
buttonPlus.grid(row=3,column=3)

buttonminus = Button(frame,
                    text= "-",
                    width=8,
                    height=3,
                    font=35,
                    command=lambda:button_press('-')
                        )
buttonminus.grid(row=2,column=3)


buttonMultipication = Button(frame,
                    text= "X",
                    width=8,
                    height=3,
                    font=35,
                    command=lambda:button_press('*')
                        )
buttonMultipication.grid(row=1,column=3)

buttonDivision = Button(frame,
                    text= 	"\u00f7",
                    width=8,
                    height=3,
                    font=35,
                    command=lambda:button_press('/')
                        )
buttonDivision.grid(row=0,column=3)


buttonEqual = Button(frame,
                    text= "=",
                    width=8,
                    height=3,
                    font=35,
                    command=equation
                        )
buttonEqual.grid(row=3,column=2)

buttonClear = Button(root,
                    text= "clear",
                    
                    height=3,
                    font=35,
                    command=clear
                        )
buttonClear.pack(fill=X)








root.mainloop()

