from tkinter import T,Button
root=Tk()
def mycallback():
    print("you clicked the msg button")
msgbut=Button(root,text="click Here",Command=mycallback()
msgbut.pack()
root.mainloop()
