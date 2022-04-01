from tkinter import *
import smtplib
import cr
m=Tk()
m.title("PARKME")
m.geometry("600x500")
label=Label(m,text="PARK ME!!!",font=("arial black",20))
label.grid(row=1,column=2)
e=Entry(m,width=20)
e1=Entry(m,width=20)
e2=Entry(m,width=20)
e3=Entry(m,width=10)
e4=Entry(m,width=10)
e5=Entry(m,width=20)
e.grid(row=3,column=1)
e1.grid(row=4,column=1)
e2.grid(row=5,column=1)
e3.grid(row=7,column=1)
e4.grid(row=7,column=3)
e5.grid(row=12,column=1)
def mail(to,mail):
    s=smtplib.SMTP('smpt.gmail.com',587)
    s.starttls()
    s.login(cr.ma,cr.pa)
    s.sendmail(cr.ma,to,mail)
    s.quit()

l=Label(m,text="NAME :")
lab=Label(m,text="PHONE :")
l2=Label(m,text="VEHICLE REG NO :")
l3=Label(m,text="ENTRY TIME :")
l4=Label(m,text="EXIT TIME:")
l5=Label(m,text="AVAILABLE SLOTS :")
l6=Label(m,text="EMAIL:")

l.grid(row=3,column=0)
lab.grid(row=4,column=0)
l2.grid(row=5,column=0)
l3.grid(row=7,column=0)
l4.grid(row=7,column=4)
l6.grid(row=12,column=0)
d1=IntVar(m,e3.get())


options =['SLOT 1',
          'SLOT 2',
          'SLOT 3',
          'SLOT 4',
          'SLOT 5',
          'SLOT 6']
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(m,clicked,*options)
options1 =['AM',
          'PM']
clicked1 = StringVar()
clicked1.set(options1[0])
drop1 = OptionMenu(m,clicked1,*options1)
options2 =['AM',
          'PM']
clicked2 = StringVar()
clicked2.set(options2[0])
drop2 = OptionMenu(m,clicked2,*options2)

def calc():
    r=d1
    
    la=Label(m,text = e.get()+" YOUR "+(clicked).get()+" HAS BEEN CONFIRMED ")
    c=int(e3.get())
    d=c*20
    lb=Label(m,text = "YOUR TOTAL BILL IS "+str(d)+"Rupees")
    
    la.grid(row=10,column=0)
    lb.grid(row=11,column=0)

l5.grid(row=6,column=0)
drop.grid(row=6,column=1,padx=20,pady=20)
drop1.grid(row=7,column=2)
drop2.grid(row=7,column=5)
b=Button(m,text="ENTER",command=calc)
r=e.get()+" YOUR "+(clicked).get()+" HAS BEEN CONFIRMED "
b1=Button(m,text="confirm",command=lambda :mail(e5.get(),r))
la1=Label(m,text =r)
la1.grid(row=14,column=0)
b.grid(row=9,column=0)
b1.grid(row=13,column=0)

m.mainloop()
