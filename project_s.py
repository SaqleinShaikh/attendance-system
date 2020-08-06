from tkinter import *
import tkinter.messagebox 
import cv2 ,time,datetime
import e,capture
import mysql.connector


################################INTERFACE###################################
root=Tk()
root.title("Employee ATTENDANCE system")
root.geometry('1550x850+0+0')
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

####################################### Root Exit function ####################################

def exit():
  exit=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
  if exit>0:
    root.destroy()
    return
 
def insert_fun(userName,Name,mobile_No,Mail_id,Passwd,cityy,photo):
   def convertToBinaryData(filename):
      # Convert digital data to binary format
      with open(filename, 'rb') as file:
         binaryData = file.read()
      return binaryData
   flag=1
   try:
      connection = mysql.connector.connect(host='localhost',
                                             database='employee',
                                             user='root',
                                             password='S@qlein05')

      cursor = connection.cursor()
      
      sql= """select username from employee where username like %s"""
      tup_p=(userName,)
      cursor.execute(sql,tup_p)
      for i in cursor:
         flag=0
     
      if(flag==1):
         sql_insert_blob_query = """ INSERT INTO employee
                          VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
         empPicture = convertToBinaryData(photo)
         unix=time.time()
         date=str(datetime.datetime.fromtimestamp(unix).strftime("%D %H:%M:%S "))
         insert_blob_tuple = (userName,Name,mobile_No,Mail_id,Passwd,cityy,empPicture,date)
         result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
         connection.commit()
         #lblName_P=Label(fla,text="saved , press done",font=('arial',14,'bold'),bd=20,fg="red",bg="CYAN").grid(row=6,column=0)
      else:
         lblName_P=Label(fla,text="username is already taken\n try again ",font=('arial',14,'bold'),bd=20,fg="red",bg="CYAN").grid(row=6,column=0)
   except mysql.connector.Error as error:
      print("Failed inserting user data into MySQL table {}".format(error))

   finally:
      if (connection.is_connected()):
         cursor.close()
         connection.commit()
         connection.close()
   return flag

def punch_fun(UserName , UserPasswword):
   flag =0
   def convertToBinaryData(filename):
      # Convert digital data to binary format
      with open(filename, 'rb') as file:
         binaryData = file.read()
      return binaryData

   try:
      connection = mysql.connector.connect(host='localhost',
                                             database='employee',
                                             user='root',
                                             password='S@qlein05')
   
      cursor = connection.cursor()
      unix=time.time()
      date=str(datetime.datetime.fromtimestamp(unix).strftime("%D %H:%M:%S "))
      sql= """select username from employee where username LIKE %s and UserPassword like %s """
      tup=(UserName,UserPasswword,)
      cursor.execute(sql,tup)
      empPicture = convertToBinaryData("C:/Users/WIN 10/vs code program/saved_img.jpg")
      tupp=(UserName,date,empPicture)
      sql_p="""insert into punch values (%s,%s,%s)"""  
      for i in cursor:
         flag=1
         capture.PHOTO_T()
         cursor.execute(sql_p,tupp)
   except mysql.connector.Error as error:
      print("Failed inserting punching data into MySQL table {}".format(error))  
    
   finally:
      if (connection.is_connected()):
         cursor.close()
         connection.commit()
         connection.close()
         print("MySQL connection is closed") 
   return flag
   
##################################### New Employee entry function #############################
def enterinfo():
   e.reset(user_name,name,passwd,mob_n,mail,city)      
   lblName=Label(fla,text="USER NAME",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=0,column=0)
   lblName=Label(fla,text="Name",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=0,column=2)
   lblAddress=Label(fla,text="MOBILE NO",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=1,column=0) 
   lblEmployer=Label(fla,text="EMAIL ID",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=1,column=2)
   lblNINumber=Label(fla,text="PASSWORD",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=2,column=0)
   lblNINumber=Label(fla,text="City",font=('arial',16,'bold'),bd=20,fg="BLACK",bg="WHITE").grid(row=2,column=2)

   etxhoursworked=Entry(fla,textvariable=passwd,font=('arial',16,'bold'),bd=16,width=22,justify='left',show='*')
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

       
   def update_info():                                                       # update function of following save button
      txtpayslip.delete("1.0",END)
      txtpayslip.insert(END,"\tEMPLOYEE INFORMATION\n\n")
      txtpayslip.insert(END,"USER NAME :\t"+user_name.get()+"\n\n")
      txtpayslip.insert(END,"Name :\t\t"+name.get()+"\n\n")
      txtpayslip.insert(END,"mobile number :\t\t"+mob_n.get()+"\n\n")
      txtpayslip.insert(END,"password :\t\t"+passwd.get()+"\n\n")
      txtpayslip.insert(END,"mail id :\t"+mail.get()+"\n\n")
      txtpayslip.insert(END,"City :\t"+city.get()+"\n\n")
      user_n=user_name.get()
      namee=name.get()
      mob=mob_n.get()
      maild=mail.get()
      passs=passwd.get()   
      cityy=city.get()
      #capture.PHOTO_T()
      flag = insert_fun(user_n,namee,mob,maild,passs,cityy,"C:/Users/WIN 10/vs code program/saved_img.jpg")
      lblName_Pp=Label(fla,text="Please wait..while processing",font=('arial',14,'bold'),bd=20,fg="red",bg="CYAN").grid(row=6,column=0)
      #e.email_entry(maild)
      lblName_P=Label(fla,text="Entry is saved , press done",font=('arial',14,'bold'),bd=20,fg="red",bg="CYAN").grid(row=6,column=0)
      def doned_entry():
         root.destroy()
      if(flag==1):
         capture.PHOTO_T()
         btn_conp=Button(fla,text='Done',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=doned_entry,fg="red",bg="WHITE").grid(row=3,column=2)
      else:
         btn_conp=Button(fla,text='Username is already taken',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=doned_entry,fg="red",bg="WHITE").grid(row=3,column=2)          
   btnsave=Button(fla,text='SAVE',padx=25,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=update_info,fg="BLACK",bg="WHITE").grid(row=3,column=3)        # save button of root entry interfcae


############################################################   punching function #########################
def punch():
   ch_user=StringVar()
   ch_pass=StringVar()
   root_t=Tk()
   root_t.title("WELCOME TO PUNCHING PROCESS")
   root_t.geometry('1550x850+0+0')
   root_t.configure(background="CYAN")
 
   def exit_p():                   # exit function of punching interface , it is nested function
      exit_p=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
      if exit_p>0:
         root_t.destroy()
         return

   f3=Frame(root_t,width=600,height=600,bd=8,bg="WHITE")
   f3.pack(side=LEFT)
   
   flc=Frame(f3,width=600,height=200,bd=8,bg="CYAN")
   flc.pack(side=TOP)  

   btn_exit=Button(flc,text='Exit',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=exit_p,fg="red",bg="WHITE").grid(row=4,column=5) ##Exit Button of punching interface 
   lblName_p=Label(flc,text="Username",font=('arial',16,'bold'),bd=20,fg="red",bg="CYAN").grid(row=0,column=0) # enter user name label 
   e_usr=Entry(flc,textvariable=ch_user,font=('arial',16,'bold'),bd=16,width=30,justify='left')               # entry field of user name of punching 
   e_usr.grid(row=0,column=1)
   lblName_P=Label(flc,text="Password",font=('arial',16,'bold'),bd=20,fg="red",bg="CYAN").grid(row=1,column=0) #enter password label of punching field 
   e_pass=Entry(flc,textvariable=ch_pass,font=('arial',16,'bold'),bd=16,width=30,justify='left',show='*')                          # entry field of password   
   e_pass.grid(row=1,column=1)

   def con():
      flag=punch_fun(e_usr.get(),e_pass.get())
      if(flag==1):
         lblName_P=Label(flc,text="Your Punching is Successful ,Press Done to Save",font=('arial',16,'bold'),bd=20,fg="red",bg="CYAN").grid(row=6,column=0)
         btn_conp=Button(flc,text='Done',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=doned,fg="red",bg="WHITE").grid(row=3,column=2)   # after entering password done button is here
      else:
         lblName_P=Label(flc,text="Invalid Credintials , Please try again",font=('arial',16,'bold'),bd=20,fg="red",bg="CYAN").grid(row=6,column=0)


   def doned():
      root.destroy()
      e.email_punching(e_usr.get())
      root_t.destroy()
   btn_conp=Button(flc,text='Submit',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=con,fg="red",bg="WHITE").grid(row=4,column=2)    # next button to process after entering username 


#####################################################  Intilizing variables ###########################################
user_name=StringVar()
name=StringVar()
passwd=StringVar()
mob_n=StringVar()
mail=StringVar()
city=StringVar()

#########################Display process##########################
  
txtpayslip=Text(f2,height=22,width=40,bd=16,font=('arial',13,'bold'),fg="green",bg="powder blue")
txtpayslip.grid(row=1,column=0)

#===============================root (New entry ) main buttons ================================s===============================

btnreset=Button(flb,text='NEW ENTRY',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=enterinfo,fg="red",bg="powder blue").grid(row=0,column=2)  

btnpayslip=Button(flb,text='PUNCHING',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=punch,fg="red",bg="powder blue").grid(row=0,column=4)

btnexit=Button(flb,text='Exit System',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=exit,fg="red",bg="powder blue").grid(row=0,column=6)

root.mainloop()
