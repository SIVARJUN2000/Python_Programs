from tkinter import Tk,Button
root=Tk()
def mycallback():
    print("you clicked the msg button")
msgbut=Button(root,text="click Here",command=mycallback())
msgbut.pack()
root.mainloop()
