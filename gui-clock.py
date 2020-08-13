from tkinter import*
import time

root = Tk()
root.title("digital clock")
root.geometry("1350x600+300+160")
root.config(bg = "#081923")

def guiclock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))

    def config():
        lbl_hr=Label(root,text=h,font=("times new roman",50,"bold"),bg="#0875B7",fg='white')
        lbl_hr.place(x=350,y=200,width=150,height=150)

        lbl_hr2=Label(root,text='HOURS',font=("times new roman",20,"bold"),bg="#0875B7",fg='white')
        lbl_hr2.place(x=350,y=360,width=150,height=50)

        lbl_mn=Label(root,text=m,font=("times new roman",50,"bold"),bg="#008EA4",fg='white')
        lbl_mn.place(x=520,y=200,width=150,height=150)

        lbl_mn2=Label(root,text='MINUTE',font=("times new roman",20,"bold"),bg="#008EA4",fg='white')
        lbl_mn2.place(x=520,y=360,width=150,height=50)

        lbl_se=Label(root,text=s,font=("times new roman",50,"bold"),bg="#DF002A",fg='white')
        lbl_se.place(x=690,y=200,width=150,height=150)

        lbl_se2=Label(root,text='SECONDS',font=("times new roman",20,"bold"),bg="#DF002A",fg='white')
        lbl_se2.place(x=690,y=360,width=150,height=50)

        lbl_am=Label(root,text='AM',font=("times new roman",50,"bold"),bg="#DF002A",fg='white')
        lbl_am.place(x=860,y=200,width=150,height=150)

        lbl_am2=Label(root,text='NOON',font=("times new roman",20,"bold"),bg="#DF002A",fg='white')
        lbl_am2.place(x=860,y=360,width=150,height=50)

    config()


guiclock()

root.mainloop()