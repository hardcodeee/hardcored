from tkinter import *
import smtplib
import math, random

m=Tk()
m.title("PARKME")
m.geometry("600x500")
label=Label(m,text="PARK ME!!!",font=("arial black",20))
label.grid(row=1,column=2)
entry=Entry(m,width=20)
entry1=Entry(m,width=20)
entry2=Entry(m,width=20)
entry3=Entry(m,width=10)
entry4=Entry(m,width=10)
entry5=Entry(m,width=20)
entry.grid(row=3,column=1) 
entry1.grid(row=4,column=1)
entry2.grid(row=5,column=1)
entry3.grid(row=7,column=1)
entry4.grid(row=7,column=3)
entry5.grid(row=12,column=1)


label=Label(m,text="PHONE :")
lab=Label(m,text="NAME :")
label2=Label(m,text="VEHICLE REG NO :")
label3=Label(m,text="TOTAL TIME")
label4=Label(m,text="ENTRY TIME")

label6=Label(m,text="EMAIL:")

label.grid(row=3,column=0)

lab.grid(row=4,column=0)
label2.grid(row=5,column=0)
label3.grid(row=7,column=0)
label4.grid(row=7,column=4)
label6.grid(row=12,column=0)



options2 =['AM',
          'PM']
clicked2 = StringVar()
clicked2.set(options2[0])
drop2 = OptionMenu(m,clicked2,*options2)
r=str(entry1.get())
r1=" YOUR SLOT HAS BEEN CONFIRMED "
def send_message():
    calc()
    address_info = entry5.get()
    
    email_body_info =r1
    
    
    
    sender_email = "parkme022@gmail.com"
    
    sender_password = "parkMe@2022"
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.starttls()
    
    server.login(sender_email,sender_password)
    server.sendmail(sender_email,address_info,email_body_info)
def generateOTP() :
  string = '0123456789'
  OTP = ""
  length = len(string)
  for i in range(6) :
     OTP += string[math.floor(random.random() * length)]
 
  return OTP 
otp=generateOTP()
def otpgen():
    o=Label(m,text="ENTER THE OTP") 
    o.grid(row=14,column=0)
    entry6=Entry(m,width=20)
    entry6.grid(row=14,column=1)
    if(entry6.get()==otp):
      send_otp()
    else:
        lb1=Label(m,text ="error" )
        lb1.grid(row=15,column=0)

def send_otp():
    calc()
    address_info = entry5.get()
    
    email_body_info =otp
    
    
    
    sender_email = "parkme022@gmail.com"
    
    sender_password = "parkMe@2022"
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.starttls()
    
    server.login(sender_email,sender_password)
    server.sendmail(sender_email,address_info,email_body_info)



 

def calc():
    
    

    la=Label(m,text = r)
    c=int(entry3.get())
    d=c*20
    r2="YOUR TOTAL BILL IS "+str(d)+"Rupees"
    lb=Label(m,text =r2 )
    
    la.grid(row=10,column=0)
    lb.grid(row=11,column=0)
    

drop2.grid(row=7,column=5)
b1=Button(m,text="confirm",command=lambda :otpgen())

b1.grid(row=13,column=0)

m.mainloop()
