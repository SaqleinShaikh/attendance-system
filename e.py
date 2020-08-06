from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import email.message
import smtplib
import mysql.connector
from datetime import datetime


def email_entry(email_get):
   # create message object instance
   msg = MIMEMultipart()
   msg = email.message.Message()
   msg['Subject'] = 'Entry saved '

   email_content = """
   <html>
   <head>
    
   <title>Employee Entry Email </title>
   <style type="text/css">
    a {color: #d80a3e;}
   body, #header h1, #header h2, p {margin: 0; padding: 0;}
   #main {border: 1px solid #cfcece;}
   img {display: block;}
   #top-message p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
   #bottom p {color: blue; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
   #header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
   #header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
   h5 {margin: 0 0 0.8em 0;}
   h5 {font-size: 18px; color: red !important; font-family: Arial, Helvetica, sans-serif; }
   </style>
   </head>
   <body>
   <table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>
   <table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
   <tr>
      <td align="center">
        <p><a href="#">View in Browser</a></p>
      </td>
    </tr>
   </table>
 
    <table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
    <tr>
      <td>
        <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
          <tr>
            <td width="570" align="center"  bgcolor="#d80a3e"><h1>Employee attendance system</h1></td>
          </tr>
          <tr>
            <td width="570" align="right" bgcolor="#d80a3e"><p>June 2020</p></td>
          </tr>
        </table>
      </td>
    </tr>
     
    <tr>
      <td>
        <table id="content-3" cellpadding="0" cellspacing="0" align="center">
          <tr>
              <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
              <img src="https://saqleinshaikh.000webhostapp.com/wp-content/uploads/2018/12/about_img.jpg" width="550" height="150"  />
            </td>
			<td width="15"></td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td>
        <table id="content-4" cellpadding="0" cellspacing="0" align="center">
          <tr>
            <td width="350" valign="top">
              <h5 >Account is created succesfully </h5><h5>Entry is Saved </h5>
              <p>Dear User your data in employee attendance system is successfully created.</p>
			  <p>We wish you a great Journey ahead with a Company.</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
    </table>
    <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
    <tr>
      <td align="center">
        <p id="reference">Design and maintained by Saqlein Shaikh</p>
      </td>
    </tr>
    </table><!-- top message -->
    </td></tr></table><!-- wrapper -->
 
    </body>
    </html>
    """


   # setup the parameters of the message
   password = "Sh@bana05"
   msg['From'] = "saqleinsheikh43@gmail.com" 
   msg['To'] = email_get
   msg['Subject'] = "Photos"
   headers = list((k, v) for (k, v) in msg.items() if k not in ("Content-Type", "Content-Transfer-Encoding"))
   msg.add_header('Content-Type', 'text/html')
   msg.set_payload(email_content)

   # create server
   server = smtplib.SMTP('smtp.gmail.com: 587')
   server.starttls()
   # Login Credentials for sending the mail
   server.login(msg['From'], password)
   # send the message via the server.
   server.sendmail(msg['From'], msg['To'], msg.as_string())
   server.quit()
   print("successfully sent email to %s:" % (msg['To']))

def email_punching(ename_p):
   connection = mysql.connector.connect(host='localhost',
                                             database='employee',
                                             user='root',
                                             password='S@qlein05')
   sql_query="""select email_id from employee where username like %s"""
   var=(ename_p,)   
   cursor = connection.cursor()
   cursor.execute(sql_query,var)
   for i in cursor:
      mail_id=i                             
   
   now_p = datetime.now()
   dt_stringg = now_p.strftime("%d/%m/%Y  \t%H:%M:%S")
   print("in process mail")   
   s = smtplib.SMTP('smtp.gmail.com', 587) 
   s.starttls()
   print("punching mail is in process") 
   s.login("saqleinsheikh43@gmail.com", "Sh@bana05") 
   mail_pp=mail_id
   message = "subject:punching confirm \n\nDear " + ename_p + " \n\n\tyour punching is succesfully recorded of date \n\n"+ dt_stringg +"\n\n\t\t[ HAVE A GOOD DAY ]"+"\n\n\n\nManaged by:-\nSaqlein shaikh"
   #msg.attach(MIMEImage(file("google.jpg").read()))
   s.sendmail("Employee.Attenddance.System@gmail.com", mail_pp, message)
   print("\nsuccesfully sent") 
   s.quit()

def reset(user_name,name,passwd,mob_n,mail,city):
  user_name.set("")
  name.set("")
  passwd.set("")
  mob_n.set("")
  mail.set("")
  city.set("")

