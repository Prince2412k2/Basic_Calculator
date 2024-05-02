from tkinter import *

root=Tk()

root.title("calculator")
ans=0
history=""


#functions


def anspos():
    global ans
    global history
    if (ans)==0 and len(history)==1:
        ans=1

def hist_ref():
        global history
        global ans
        h.config(state="normal")
        h.delete(0,END)
        h.config(width=len(history) + 2)
        h.insert(0,history)
        h.config(state="readonly")

        a.config(state="normal")
        a.delete(0,END)
        a.config(width=len(str(ans)) + 5) 
        a.insert(0,f"={ans}")
        a.config(state="readonly")

def addition():
    try:
        global history
        global ans
        ans+=float(e.get())
        history=history + "+" + e.get()
        hist_ref()
        e.delete(0,END)
    except ValueError:
        return 0
    
def subtraction():
    try:
        global history
        global ans
        ans-=float(e.get())
        history=history + "-" + e.get()
        hist_ref()
        e.delete(0,END)
    except ValueError:
        return 0

def division():

    if e.get()=="":
        return 0
    anspos()
    if e.get()=="1":
        return 0
    try:
        global history
        global ans
        ans/=float(e.get())
        history=f"({history})" + "/" + f"({e.get()})"
        hist_ref()
        e.delete(0,END)
    except ValueError:
        print("Error occured in division")
        return 0

def multiplication():

    anspos()
    if e.get()=="1":
        return 0
    try:
        global history
        global ans
        ans*=float(e.get())
        history=f"({history})" + "*" + f"({e.get()})"
        hist_ref()
        e.delete(0,END)
    except ValueError:
        return 0
    
def power():
    if e.get()=="":
        return 0
    anspos()
    if e.get()=="1":
        return 0
    try:
        global history
        global ans
        temp_ans=ans
        try:
            for i in range(int(e.get())-1):
                ans*=int(temp_ans)
        except ValueError :
            print("Error occured in power")
        history=f"({history})" + "^" + f"({e.get()})"
        hist_ref()
        e.delete(0,END)
    except ValueError:
        return 0


# #taking input keys
# root.bind("<Key>", keyput)

#history window
h=Entry(root,width=2)
h.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
h.config(state="readonly")

#entry window
e=Entry(root,width=35, borderwidth=3)
e.grid(row=2,column=0,columnspan=3,padx=10,pady=10)

#answer window
a=Entry(root,width=5)
a.grid(row=1,column=0,columnspan=3,padx=10,pady=10)
a.config(state="readonly")

#buttons
add= Button(root,text="+", width=2,height=1,padx=40,pady=20, command=addition)
sub= Button(root,text="-", width=2,height=1,padx=40,pady=20, command=subtraction)
div= Button(root,text="/", padx=40,pady=20, command=division)
multi= Button(root,text="*", padx=40,pady=20, command=multiplication)
powerr= Button(root,text="^", padx=40,pady=20, command=power)

#aligning the buttons
add.grid(row=3,column=0,columnspan=1,padx=10,pady=10)
sub.grid(row=3,column=2,columnspan=1,padx=10,pady=10)
div.grid(row=4,column=0,columnspan=1,padx=10,pady=10)
multi.grid(row=4,column=2,columnspan=1,padx=10,pady=10)
powerr.grid(row=5,column=1,columnspan=1,padx=10,pady=10)

root.mainloop()    


