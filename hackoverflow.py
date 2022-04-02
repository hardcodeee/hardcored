from tkinter import *
import smtplib
import math, random

tkinter=Tk()
tkinter.title("PARKME")
tkinter.geometry("500x400")
first_title=Label(tkinter,text="PARK ME!!!",font=("arial black",20))
first_title.grid(row=1,column=1)
name=Entry(tkinter,width=20)
phone=Entry(tkinter,width=20)
vehiclereg_no=Entry(tkinter,width=20)
Entry_time=Entry(tkinter,width=20)
email_id=Entry(tkinter,width=20)
name.grid(row=3,column=1) 
phone.grid(row=4,column=1)
vehiclereg_no.grid(row=5,column=1)
Entry_time.grid(row=7,column=1)
email_id.grid(row=12,column=1)


first_title=Label(tkinter,text="NAME :")
lab=Label(tkinter,text="PHONE NO :")
label2=Label(tkinter,text="VEHICLE REG NO :")
label3=Label(tkinter,text="ENTRY TIME")

label6=Label(tkinter,text="EMAIL:")

first_title.grid(row=3,column=0)

lab.grid(row=4,column=0)
label2.grid(row=5,column=0)
label3.grid(row=7,column=0)
label6.grid(row=12,column=0)



options2 =['AM',
          'PM']
clicked2 = StringVar()
clicked2.set(options2[0])
drop2 = OptionMenu(tkinter,clicked2,*options2)

def generateOTP() :
  string = '0123456789'
  OTP = ""
  length = len(string)
  for i in range(6) :
     OTP += string[math.floor(random.random() * length)]
 
  return OTP 
otp=generateOTP()
temp=""
m="CONFIRMATION MAIL:  \n"+otp+"  IS YOUR OTP PLEASE ENTER THE OTP FOR CONFIRMATION"

def send_otp():
    
    address_info = email_id.get()
    
    email_body_info ="HEY "+name.get()+"\n"+m
    
    
    
    sender_email = "parkme022@gmail.com"
    
    sender_password = "parkMe@2022"
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.starttls()
    
    server.login(sender_email,sender_password)
    server.sendmail(sender_email,address_info,email_body_info)
    calc()
    confrm()

def confrm():
    otp_i=Entry(tkinter,width=20)
    otp_i.grid(row=16,column=1)
    otp_l=Label(tkinter,text="ENTER THE OTP")
    otp_l.grid(row=16,column=0)
    temp=otp_i.get()
    b2=Button(tkinter,text="confirm",command=check())
    b2.grid(row=17,column=0)
def check():
    if(otp==temp):
       confirm=Label(tkinter,text="YOUR SLOT IS BOOKED")
       print("arshan")
    else:
       confirm=Label(tkinter,text="SORRY INVALID INPUT")

    
        
def calc():
    
    

    la=Label(tkinter,text = "THE OTP HAS BEEN SEND TO YOUR MAIL")
    
    
    la.grid(row=15,column=0)
    

drop2.grid(row=7,column=2)
b1=Button(tkinter,text="confirm",command=lambda :send_otp())
b1.grid(row=13,column=0)



tkinter.mainloop()
