from tkinter import *
w = Tk()
w.geometry('350x350')
def red():
    w.config(bg='red')
    print('color:red')
def green():
    w.config(bg="green")
    print('color:green')
def bleu():
    w.config(bg="blue")
    print('color:blue')
def yel():
    w.config(bg="yellow")
    print('color:yellow')
def bl():
    w.config(bg="black")
    print('color:black')
def whit():
    w.config(bg='white')
    print('color:white')
def cyan():
    w.config(bg="cyan")
    print('color:cyan')
def pink():
    w.config(bg="pink")
    print('color:pink')
def orange():
    w.config(bg="orange")
    print('color:orange')
def gray():
    w.config(bg='gray')
    print('color:grey')

btnred= Button(w,text="red",bg="red", command=red)
btnred.pack()

btngreen= Button(w,text="green",bg="green", command=green)
btngreen.pack()

btnblue= Button(w,text="blue",bg="blue", command=bleu)
btnblue.pack()

btnyel= Button(w,text="yellow",bg="yellow", command=yel)
btnyel.pack()

btnbla= Button(w,text="black",bg="black",fg="white", command=bl)
btnbla.pack()

btnwhit= Button(w,text="white",bg="white", command=whit)
btnwhit.pack()

btncyan= Button(w,text="cyan",bg="cyan", command=cyan)
btncyan.pack()

btnpink= Button(w,text="pink",bg="pink", command=pink)
btnpink.pack()

btnora= Button(w,text="orange",bg="orange", command=orange)
btnora.pack()

btngray= Button(w,text="gray",bg="gray", command=gray)
btngray.pack()

mainloop()