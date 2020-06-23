# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:57:33 2020

@author: northner
"""
from time import sleep
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
from colorama import Fore, Back, Style
from getpass import getpass
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
cprint(figlet_format('K n o c k - K n o c k', font='starwars'),
       'green', attrs=['bold'])

st1="A face detection and recognization system"
st2="~by NorthNer" 
print(Fore.YELLOW + bcolors.UNDERLINE +bcolors.BOLD +Back.GREEN+st1+ bcolors.ENDC+"          "+ Fore.BLUE+Back.BLACK+Style.BRIGHT+st2+ bcolors.ENDC)
print("")
print("")
st="Enter your choice-"
for x in st :
    print(bcolors.BOLD+Fore.MAGENTA +x , end='' + bcolors.ENDC)
    sys.stdout.flush()
    sleep(0.1)
print("")
print("")
print(Fore.RED +Back.WHITE+" <1>."+Fore.WHITE +Back.BLUE+ "  Start Attendance/Search")
print(" " )
print(Fore.RED +Back.WHITE+" <2>."+Fore.WHITE +Back.BLUE+ "  Train the Classifier")
print(" " )
print(Fore.RED +Back.WHITE+" <3>."+Fore.WHITE +Back.BLUE+ "  Add images to the Dataset" )
print("")
print(Fore.RED +Back.WHITE+" <4>."+Fore.WHITE +Back.BLUE+ "  Send the attendance Via eMail" )
print("")
print("[INFO] Press"+Fore.RED +Back.WHITE+" <q> "+Fore.WHITE +Back.BLUE+ "to Exit")
      

while True:

    z=input()
    if z == "q":
        break

    if (z=='1'):
        import faces
        faces
    elif (z=='2'):
        import facestrain

        facestrain
    elif (z=='3'):
        import dataset
        dataset
    elif(z=='4'):
        fromaddr =input("EMAIL address of the <sender>\n> ")
        toaddr = input( "EMAIL address of the <receiver> \n> ")
        
        msg = MIMEMultipart() 
        msg['From'] = fromaddr 

        msg['To'] = toaddr  
        body = "This is a mail of the attendance."
        msg.attach(MIMEText(body, 'plain'))  
        filename = "attendance.csv"
        attachment = open("attendance.csv", "rb") 
        p = MIMEBase('application', 'octet-stream') 
        p.set_payload((attachment).read()) 
        encoders.encode_base64(p) #encode payload in base 64
   
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p) 
        s = smtplib.SMTP('smtp.gmail.com', 587) #smtp session creation
        s.starttls() #start TLS for security
        password = getpass("Enter your <P @ $ 5 W 0 R D>\n \n[INFO] while entring password the screen will be blank no character will appear\n# ")
        s.login(fromaddr, password) #authentication
        text = msg.as_string() 
        s.sendmail(fromaddr, toaddr, text) #sending mail
        s.quit() #session end
    else:
        print(Back.WHITE+Fore.RED+"PLEASE ENTER THE VALID OPTION")

