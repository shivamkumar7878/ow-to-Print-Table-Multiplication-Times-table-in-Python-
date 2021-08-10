from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Print Table')
root.geometry('1280x720')

#==========================variable======================
var=StringVar()
#=============================function===============
def mul():
    txtResult.delete(1.0,END)
    m=var.get()
    if m.isdigit():
        m=int(m)
        for i in range(1,11):
            txtResult.insert(END,'\n\t')
            txtResult.insert(END,m,'\t','X','\t',i,'\t','=','\t',(m*i))
            txtResult.insert(END,'\n')
        return True
    else:
        messagebox.showwarning('Error','Invalid Data ,Please Enter Number')
        var.set('')
        return False

def Reset():
    if messagebox.askyesno('Multiplication Table','Confirm if you want to Reset'):
        txtResult.delete(1.0,END)
        var.set('')

def Exit():
    if messagebox.askyesno('Multiplication Table','Confirm if you want to Quit'):
        root.destroy()
    else:
        txtResult.delete(1.0,END)
        var.set('')


#================================Frame============================
f=Frame(root,bg='cadetblue',relief=RIDGE,padx=30,pady=30)
f.grid()
lf=Frame(f,bd=7,width=500,height=600,relief=RIDGE)
lf.grid(row=0,column=0,padx=30)

Rf=Frame(f,bd=7,width=500,height=600,relief=RIDGE)
Rf.grid(row=0,column=1,padx=30)

#=========================Entry and Label========================
titleLabel=Label(Rf,text='Muliplication Table',font='arial 40 bold',bg='yellow',fg='crimson')
titleLabel.grid(row=0,column=0,padx=30,pady=20)

txtResult=Text(Rf,font='arial 13 bold',bd=10,width=30,height=23)
txtResult.grid(row=1,column=0,pady=20)

title=Label(lf,text='Enter A Number',font='arial 40 bold',bg='yellow',fg='crimson')
title.grid(row=0,column=0,padx=30,pady=20)

e=Entry(lf,font='arial 20 bold',textvariable=var,bd=10,justify='center')
e.grid(row=1,column=0,pady=20)

#=================================Button==========================
bt1=Button(lf,text='Multiplication',font='arial 20 bold',bg='lime',bd=10,width=16,command=mul)
bt1.grid(row=2,column=0,pady=20)
bt2=Button(lf,text='Reset',font='arial 20 bold',bg='lime',bd=10,width=16,command=Reset)
bt2.grid(row=3,column=0,pady=20)
bt3=Button(lf,text='Exit',font='arial 20 bold',bg='lime',bd=10,width=16,command=Exit)
bt3.grid(row=4,column=0,pady=20)

'''icon=PhotoImage(file='p.png')
root.iconphoto(True,icon)
root.config(background="black")
'''
root.mainloop()