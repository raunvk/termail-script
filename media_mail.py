import sys
import smtplib
import getpass
import webbrowser
import imghdr
from email.message import EmailMessage

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

try:
	file1 = open('media_mail.txt', 'r')
	print(' ')
	print (bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print('\nBanner File not found!!!')


userid = input("\nEnter your G-Mail id :\t")
passwd = getpass.getpass("\nEnter your Password :\t")
target = input("\nEnter target G-Mail id :\t")
subj = input("\nEnter the Subject (optional) :\n\n")
body = input("\nEnter the Message :\n\n")


msg = EmailMessage()
msg["Subject"] = subj
msg["From"] = userid
msg["To"] = target
msg.set_content(body)

media = input("\nDo you want to attach any Media File (y/n)?\n\n")

if(media == "y" or media == "Y"):
	choice = int(input("\nEnter Media File type :\n\nPress 1 for IMG file.\nPress 2 for PDF file.\nPress 3 for HTML file.\n\n"))

	if (choice == 1):
		n = int(input("\nEnter no. of IMG file(s) you want to attach :\t"))
		for i in range (0,n):
			img = input("\nEnter IMG filepath no." + str(i+1) + " :\t")
			try:
				f = open(img, "rb")
			except:
				print("\nNo file found!!!\n")
				sys.exit(0)
			with open(img, "rb") as f:
				file_data = f.read()
				file_type = imghdr.what(f.name)
				file_name = f.name
			msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)
			print("\nAttached " + str(i+1) + " IMG file(S)!!!\n")
		print("\nPlease Wait!!!\n")

	elif (choice == 2):
		n = int(input("\nEnter no. of PDF file(s) you want to attach :\t"))
		for i in range (0,n):
			pdf = input("\nEnter PDF filepath no." + str(i+1) + " :\t")
			try:
				f = open(pdf, "rb")
			except:
				print("\nNo file found!!!\n")
				sys.exit(0)
			with open(pdf, "rb") as f:
				file_data = f.read()
				file_name = f.name
			msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
			print("\nAttached " + str(i+1) + " PDF file(s)!!!\n")
		print("\nPlease Wait!!!\n")


	else :
		print("\nWrong choice!!!\n")


else:
	print("\nNo Media File attached!!!\n")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
	try:
		smtp.login(userid, passwd)
	except smtplib.SMTPAuthenticationError:
		print("\nYour G-Mail id or Password maybe incorrect!!!\n")
		print("\nOr maybe you have disabled Less-Secure-Apps on your G-Mail account!!!\n")
		resp = int(input("\nEnter 1 to enable Less-Secure-Apps now or Enter 0 to ignore :\n\n"))
		if (resp == 1):
			webbrowser.open('http://myaccount.google.com/lesssecureapps', new=2)
			sys.exit()

	try:
		smtp.send_message(msg)
		print ("\nSuccessfully sent Mail!!!\n")
	except KeyboardInterrupt:
		print ("\nCanceled!!!\n")
		sys.exit()
	except:
		print ("\nFailed to Send!!!\n")









