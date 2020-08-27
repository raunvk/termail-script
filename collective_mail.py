import smtplib
import webbrowser
import sys
import time
import getpass
from colored import fg, bg, attr

color = fg('green')
reset = attr('reset')

try:
	file1 = open('collective_mail.txt', 'r')
	print(' ')
	print (color + file1.read() + reset)
	file1.close()
except IOError:
	print('\nBanner File not found!')

userid = input("\nEnter your G-Mail id :\t")
passwd = getpass.getpass("\nEnter your Password :\t")
subj = input("\nEnter the Subject (optional) :\n\n")
body = input("\nEnter the Message :\n\n")
message = ("From :\t" + userid + "\nSubject :\t" + subj + "\n" + body)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

try:
	server.login(userid, passwd)
except smtplib.SMTPAuthenticationError:
	print("\nYour G-Mail id or Password maybe incorrect!!!\n") 
	print("\nOr maybe you have disabled Less-Secure-Apps on your G-Mail account!!!\n")
	resp = int(input("\nEnter 1 to enable Less-Secure-Apps now or Enter 0 to ignore :\n\n"))
	if (resp == 1):
		webbrowser.open('http://myaccount.google.com/lesssecureapps', new=2) 
		sys.exit()

n = int(input("\nEnter no. of G-Mail accounts you want to send this mail to :\t"))

for i in range (0,n):
	target = input("\nEnter G-Mail id no." + str(i+1) + " :\t")
	try:
		server.sendmail(userid, target, message)
		print ("\nSuccessfully sent Mail to " + str(i+1) + " Account !!!\n")
		time.sleep(1)
	except KeyboardInterrupt:
		print ("\nCanceled!!!\n")
		sys.exit()
	except:
		print ("\nFailed to Send!!!\n")
		
server.close()
