#import the tkinter module
import tkinter as tk

#import the partial operation in functools module
from functools import partial

#create a calc function
#declare 3 variables- lab_res,n1,n2
def calc(lab_res,n1,n2):
    
    #declare num1 variable with n1 input value
    num1=(n1.get())
    
    #declare num2 variable with n2 input value
    num2=(n2.get())

    
    #use try and except concept
    try:
        lab_res=int(num1)+int(num2)
        end_result.config(text="Result is %d "%lab_res)

    except ValueError:
        end_result.config(text="Invalid input")

#create a window
win=tk.Tk()

#set window size
win.geometry("300x460+100+200")

#declare number1 datatype
number1=tk.StringVar()

#declare number2 datatype
number2=tk.StringVar()


#set window title
win.title("simple calculator")

#create a title label and use grid 
title=tk.Label(win,text="Simple Calculator...").grid(row=1,column=2)

#create label for number1 use grid
ln_1=tk.Label(win,text="Enter the first number:").grid(row=4,column=1)

#create label for number2 use grid
ln_2=tk.Label(win,text="Enter the second number:").grid(row=6,column=1)

#create entry for number1 use grid
ln_1_ent=tk.Entry(win,width=10,textvariable=number1).grid(row=4,column=2)

#create entry for number2 use grid
ln_2_ent=tk.Entry(win,width=10,textvariable=number2).grid(row=6,column=2)

#create a label for result use grid
end_result=tk.Label(win,text="")
end_result.grid(row=20,column=1)

#use partial tool asign all
calc=partial(calc,end_result,number1,number2)
#create a button use grid
btn=tk.Button(win,text="calculatoion",bg="black",fg="white",command=calc).grid(row=12,column=2)



                                                    

#call window
win.mainloop()

