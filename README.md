# employess-attendance-system
# This is python project in which i developed a project in python with user interface system.
from datetime import datetime
import array as arr
from getpass import getpass
import struct 
from tkinter import *
import tkinter.messagebox 
import smtplib
import pandas as pd 
import matplotlib.pyplot as plt 

class person(object ):
   def __init__(self, id_new, name,mob_n,passwd,mail,cityy):
      self.id_new=id_new 
      self.name = name
      self.mob_n = mob_n
      self.passwd = passwd 
      self.mail=mail
      self.cityy=cityy

class personp(object ):
   def __init__(self,ch):
      self.ch=ch



################################INTERFACE###################################
root=Tk()
root.title("Employee ATTENDANCE system")
root.geometry('1350x650+0+0')
root.configure(background="POWDER BLUE")

Tops=Frame(root,width=1350,height=50,bd=8,bg="CYAN")
Tops.pack(side=TOP)

f1=Frame(root,width=600,height=600,bd=8,bg="CYAN")
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,bd=8,bg="CYAN")
f2.pack(side=RIGHT)

fla=Frame(f1,width=600,height=200,bd=8,bg="CYAN")
fla.pack(side=TOP)

flb=Frame(f1,width=300,height=600,bd=8,bg="CYAN")
flb.pack(side=TOP)

lblinfo=Label(Tops,font=('arial',45,'bold'),text="EMPLOYEE ATTENDANCE SYSTEM ",bd=10,fg="GREEN")
lblinfo.grid(row=0,column=0)

def exit():
  exit=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
  if exit>0:
    root.destroy()
    return

personList=[]
personList_p=[]

def enterinfo():
   reset() 
       
   lblName=Label(fla,text="USER NAME",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=0,column=0)
   lblName=Label(fla,text="Name",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=0,column=2)
   lblAddress=Label(fla,text="MOBILE NO",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=1,column=0) 
   lblEmployer=Label(fla,text="EMAIL ID",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=1,column=2)
   lblNINumber=Label(fla,text="PASSWORD",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=2,column=0)
   lblNINumber=Label(fla,text="City",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=2,column=2)

   etxhoursworked=Entry(fla,textvariable=passwd,font=('arial',16,'bold'),bd=16,width=22,justify='left')
   etxhoursworked.grid(row=2,column=1)

   
   etxname=Entry(fla,textvariable=user_name,font=('arial',16,'bold'),bd=16,width=22,justify='left')
   etxname.grid(row=0,column=1)

   etxaddress=Entry(fla,textvariable=name,font=('arial',16,'bold'),bd=16,width=22,justify='left')
   etxaddress.grid(row=0,column=3)

   etxemployer=Entry(fla,textvariable=mob_n,font=('arial',16,'bold'),bd=16,width=22,justify='left')
   etxemployer.grid(row=1,column=1)

   etxhoursworked=Entry(fla,textvariable=mail,font=('arial',16,'bold'),bd=16,width=22,justify='left')
   etxhoursworked.grid(row=1,column=3)

   etxhoursworked=Entry(fla,textvariable=city,font=('arial',16,'bold'),bd=16,width=22,justify='left')
   etxhoursworked.grid(row=2,column=3)
       
   def update_info():
      txtpayslip.delete("1.0",END)
      txtpayslip.insert(END,"\tEMPLOYEE INFORMATION\n\n")
      txtpayslip.insert(END,"USER NAME :\t"+user_name.get()+"\n\n")
      txtpayslip.insert(END,"Name :\t\t"+name.get()+"\n\n")
      txtpayslip.insert(END,"mobile number :\t\t"+mob_n.get()+"\n\n")
      txtpayslip.insert(END,"password :\t\t"+passwd.get()+"\n\n")
      txtpayslip.insert(END,"mail id :\t"+mail.get()+"\n\n")
      txtpayslip.insert(END,"City :\t"+city.get()+"\n\n")
      personList.append(person(user_name.get(),name.get(),mob_n.get(),passwd.get(),mail.get(),city.get()))
      email_g(user_name.get(),name.get(),passwd.get(),mail.get(),mob_n.get(),city.get())
   btnsave=Button(fla,text='SAVE',padx=25,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=update_info,fg="BLACK",bg="WHITE").grid(row=3,column=3)   

def punch():
   for person in personList:
      print(person.cityy)
   root_t=Tk()
   root_t.title("WELCOME TO PUNCHING PROCESS")
   root_t.geometry('1350x650+0+0')
   root_t.configure(background="CYAN")
 
   def exit_p():
      exit_p=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
      if exit_p>0:
         root_t.destroy()
         return

   f3=Frame(root_t,width=600,height=600,bd=8,bg="WHITE")
   f3.pack(side=LEFT)
   f4=Frame(root_t,width=300,height=700,bd=8,bg="WHITE")
   f4.pack(side=RIGHT)
   
   flc=Frame(f3,width=600,height=200,bd=8,bg="CYAN")
   flc.pack(side=TOP)  
 
   btn_exit=Button(flc,text='Exit System',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=exit_p,fg="red",bg="WHITE").grid(row=4,column=5)  
   
   lblName_p=Label(flc,text="ENTER USER NAME",font=('arial',16,'bold'),bd=20,fg="red",bg="CYAN").grid(row=0,column=0)
   global e_usr
   e_usr=Entry(flc,textvariable=ch_user,font=('arial',16,'bold'),bd=16,width=30,justify='left')
   e_usr.grid(row=0,column=1)
        
   txtpayslip.insert(END," empty :\t"+ch_user.get()+"\n\n")
   personList_p.append(personp(ch_user.get()))
   print(ch_user.get())
   
   def con():
      lblName_P=Label(flc,text="Enter your password",font=('arial',16,'bold'),bd=20,fg="red",bg="CYAN").grid(row=1,column=0)
      e_pass=Entry(flc,textvariable=ch_pass,font=('arial',16,'bold'),bd=16,width=30,justify='left')
      e_pass.grid(row=1,column=1)
      btn_conp=Button(flc,text='DONE',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=doned,fg="red",bg="WHITE").grid(row=3,column=2) 
   def doned():
      lblName_P=Label(flc,text="YOUR PUNCHING IS SUCCESFULL",font=('arial',16,'bold'),bd=20,fg="red",bg="CYAN").grid(row=6,column=0)
      email_gf()
                
   btn_conp=Button(flc,text='NEXT',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=con,fg="red",bg="WHITE").grid(row=4,column=2)





def email_g(user_name,ename,pass_g,mail_g,mob_g,city_g):
   print("in process mail")
   global mail_pp,ename_p
   mail_pp=mail_g
   ename_p=ename   
   s = smtplib.SMTP('smtp.gmail.com', 587) 
   s.starttls()
   s.login("Employee.Attenddance.System@gmail.com", "empatt321") 
   message = "Subject:New Entry recorded \n\t\nDear " + str(ename) + " \n\n\tyour details are succesfully recorded\n\nyour User name is : " + str(user_name) +"\nyour password is: "+str(pass_g)+ "\nyour mobile number is : "+ str(mob_g) + "\nyour city is : "+ city_g + "\n\nWe are glad to see you working with us \n\n\t\t[ HAVE A GOOD DAY ]"+"\n\n\n\nManaged by:-\nSaqlein shaikh\nMahesh Sawant\nShivansh Thakur"
   s.sendmail("Employee.Attenddance.System@gmail.com", mail_g, message)
   print("\nsuccesfully sent") 
   s.quit()

def email_gf():
   now_p = datetime.now()
   global dt_stringg 
   dt_stringg = now_p.strftime("%d/%m/%Y  \t%H:%M:%S")
   print("in process mail")   
   s = smtplib.SMTP('smtp.gmail.com', 587) 
   s.starttls()
   print("punching mail is in process") 
   s.login("Employee.Attenddance.System@gmail.com", "empatt321") 
   message = "subject:punching confirm \n\nDear " + ename_p + " \n\n\tyour punching is succesfully recorded of date \n\n"+ dt_stringg +"\n\n\t\t[ HAVE A GOOD DAY ]"+"\n\n\n\nManaged by:-\nSaqlein shaikh\nMahesh Sawant\nShivansh Thakur"
   s.sendmail("Employee.Attenddance.System@gmail.com", mail_pp, message)
   print("\nsuccesfully sent") 
   s.quit()


def reset():
  user_name.set("")
  name.set("")
  passwd.set("")
  mob_n.set("")
  mail.set("")
  city.set("") 

######variables###
user_name=StringVar()
name=StringVar()
passwd=StringVar()
mob_n=StringVar()
mail=StringVar()
city=StringVar()
ch_user=StringVar()
ch_pass=StringVar()

#######date########
now = datetime.now()
global dt_string 
dt_string = now.strftime("%d/%m/%Y  \t%H:%M:%S")

#=============================== buttons ===============================================================
'''btnsalary=Button(flb,text='NEW ENTRY',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,fg="red",bg="powder blue",command=enterinfo,grid(row=0,column=0)'''

btnreset=Button(flb,text='NEW ENTRY',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=enterinfo,fg="red",bg="powder blue").grid(row=0,column=0)

btnpayslip=Button(flb,text='PUNCHING',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=punch,fg="red",bg="powder blue").grid(row=0,column=4)

btnexit=Button(flb,text='Exit System',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=exit,fg="red",bg="powder blue").grid(row=0,column=6)
#########################Display process##########################
  
txtpayslip=Text(f2,height=22,width=34,bd=16,font=('arial',13,'bold'),fg="green",bg="powder blue")
txtpayslip.grid(row=1,column=0)
  
root.mainloop()
